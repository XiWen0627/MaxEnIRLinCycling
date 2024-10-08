# _*_ coding : utf-8 _*_
# @Time : 2024-03-23 22:05
# @Author : PeterPan
# @File : DPforGridBike
# @Project : maxent_gridworld.py
# Value Iteration & Policy Iteration
from gridWalk import bicycleGridRiding
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch
import time
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

class Planner:

    def __init__(self, env, rewardFunc=None):
        self.env = env
        self.policy = None
        self.rewardFunc = rewardFunc
        if self.rewardFunc is None:
            self.rewardFunc = [self.env.rewardFunc(agentloc) for agentloc in range(len(self.env.states))]    # 此处有修改

    def initialize(self):
        self.env.reset()

    def plan(self, threshold=0.0001):
        raise Exception("Planner have to implements plan method.")

    def transitions_at(self, state, action):
        '''
        求解状态转移概率以及其相对应的奖励
        :param state:
        :param action:
        :return:
        '''
        reward = self.rewardFunc[state]
        done = state == self.env._target_location
        transition = []

        if not done:
            transition_probs = self.env.transitFunc(state, action)
            # {59: 0.028571428571428564, 11: 0.9714285714285715}
            for next_state in transition_probs:
                prob = transition_probs[next_state]
                # 59, 11
                reward = self.rewardFunc[next_state]
                done = state == self.env._target_location
                transition.append((prob, next_state, reward, done))
        else:
            transition.append((1.0, None, reward, done))

        for p, n_s, r, d in transition:
            yield p, n_s, r, d

class ValueIteration(Planner):

    def __init__(self, env, rewardFunc, gamma=0.9):
        super(ValueIteration, self).__init__(env, rewardFunc)    # 此处继承的对象有所修改
        self.gamma = gamma

    def plan(self, threshold=0.01):
        '''
        返回每个网格的最大奖励值
        '''
        self.initialize()
        actions = self.env._actions
        V = np.zeros(len(self.env.states))    # [numStates, 1]

        while True:
            delta = 0
            # The First Element of Log Array [n * nrows * ncols]
            for s in self.env.states:
                # 首先初始化各个状态的期望奖励
                # 以便于进行 Value Evaluation
                expected_rewards = []
                for a in actions:
                    reward = 0
                    for p, n_s, r, done in self.transitions_at(s, a):
                        if n_s is None:
                            reward = r    # 相应的此处的奖励函数也发生了改变
                            continue
                        # reward += p * (r + self.gamma * V[n_s] * (not done))
                        reward += p * (r + 0.9 * V[n_s] * (not done))
                    expected_rewards.append(reward)
                max_reward = max(expected_rewards)
                delta = max(delta, abs(max_reward - V[s]))
                V[s] = max_reward

            if delta < threshold:
                break

        return V

    def get_policy(self, V):
        '''
        根据状态价值函数导出一个贪婪策略
        :return: Greedy Policy
        '''
        policy = np.zeros((len(self.env.states), self.env.action_space.n))  # [numStates, numActions]

        for s in range(len(self.env.states)):
            qsa_list = []
            for a in self.env._actions:
                qsa = 0
                for p, next_state, r, done in self.transitions_at(s, a):
                    if next_state is None:
                        qsa = r
                        continue
                    else:
                        # qsa += p * (r + self.gamma * float(V[next_state]) * (1 - done))
                        qsa += p * (r + 0.9 * V[next_state] * (1 - done))

                qsa_list.append(qsa)

            # print('本脚本的 qsaList长度为 为{}'.format(len(qsa_list)))
            maxq_index = np.argmax(qsa_list)
            maxq = qsa_list[maxq_index]
            cntq = qsa_list.count(maxq)

            policy[s] = [1 / cntq if q == maxq else 0 for q in qsa_list]

        return policy

    def act(self, s):

        return np.argmax(self.policy[s])

    def policy_to_q(self, V, gamma):
        '''
        利用 Q 值进行 Policy Evaluation 的工作
        :param V: State Value
        :param gamma: Discount Rate
        :return: Action Value
        '''
        policy = self.get_policy(V)

        Q = np.zeros((len(env.states),
                      self.env.action_space.n))    # -> Q Table [numStates, numActions]

        for s in self.env.states:
            for a in self.env._actions:
                aIndex = self.env.action2Index(a)    # -> aIndex
                a_p = policy[s][aIndex]    # -> Policy [numStates, numActions]
                for p, n_s, r, done in self.transitions_at(s, a):
                    if done:
                        Q[s][aIndex] += p * a_p * r
                    else:
                        Q[s][aIndex] += p * a_p * (r + gamma * V[n_s])
        return Q

def optimal_value(env, numStates, numActions,transitionProbability,
                  reward, discount, threshold=0.01,
                  device=torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")):
    '''Find the Optimal Value Function'''
    V = torch.zeros(numStates, dtype=torch.float32).to(device)    # [numStates, 1]

    def update(s, prevDiff, V, reward, tps):
        maxV = torch.tensor(float("-inf"))
        vTemplate = torch.zeros_like(V)    # [numStates, 1]

        for a in range(numActions):
            transitProb = tps[s, a, :]    # [numStates, 1]
            maxV = max(maxV, torch.dot(transitProb, reward + discount * V))
        newDiff = abs((V[s] - maxV))
        diff = newDiff if prevDiff < newDiff else prevDiff
        vTemplate[s] = maxV

        return diff, vTemplate

    def until_converge(diff, V):
        vs = []
        outputs =[]
        for s in range(numStates):
            '''
            Optimal State Value For Each States
            '''
            diff, v = update(s=s, prevDiff=diff, V=V, reward=reward, tps=transitionProbability)

            # Append the output state to the list of outputs
            if diff < threshold:
                vs.append(v)    # [numStates, 1] -> [V[0], 0, ···, 0]
                outputs.append(diff)    # -> [numStates, 1]

        return torch.sum(torch.tensor(vs).to(device), dim=1)

if __name__ == '__main__':
    startTime = time.time()
    print('本脚本从{}开始运行···'.format(startTime))
    os.chdir(r'F:\BaiduNetdiskDownload\共享单车轨迹\共享单车轨迹\01_研究生毕业论文\1_2_DataPreProcess')
    attrTable = pd.read_csv(r'./roadPre.csv', sep=',')

    env = bicycleGridRiding(attrTable=attrTable)
    env.reset()
    print('环境已经完成构建')


    ## -----------------------------------------------
    ## --------- Test for MDP environments -----------
    ## -----------------------------------------------
    # transition_probs = env.transitFunc(1473, 1)
    # print(transition_probs)
    
    # print(1473==env._target_location)

    ## Value Iteration
    # agent = ValueIteration(env=env)
    # V_grid = agent.plan(threshold=0.01)
    # print(V_grid)
    
    # VIendTime = time.time()
    # print('本脚本需要运行的总时间为{}'.format(VIendTime-startTime))
    
    # policy = agent.get_policy(V_grid)
    # print(policy)


    # q = agent.policy_to_q(V_grid, 0.9)  # -> [numStates, numActions]
    # QTable = np.sum(q, axis=1).reshape(env.nrow, env.ncol)
    # print(QTable)  # -> Total Action Values Of Each State

    # fig, ax = plt.subplots()
    # V_grid1 = V_grid.reshape(env.nrow, env.ncol)
    # im = ax.imshow(V_grid1)
    # fig.tight_layout()
    # plt.show()
