# The Application of Maximum Entropy Deep Inverse Reinforcement Learning in Cycling.
Discovering Cyclists' Street Visual Preferences Through Multi-Source Big Data Using Deep Inverse Reinforcement Learning
# Part 1. Introduction to My Research Scenario
Our study proposes a novel framework aimed to **automatically quantify and interpret cyclists’ complicated street visual preferences from cycling records by leveraging maximum entropy deep inverse reinforcement learning(MEDIRL) and explainable artificial intelligence(XAI).** Specifically, we adapt MEDIRL model for efficient estimation of cycling reward function by integrating DBS trajectory and SVIs, which serves as a representation of cyclists’ preferences for street visual environments during routing.  

Implemented in Bantian Sub-district, Shenzhen, our framework demonstrates the feasibility and reliability of MEDIRL in discovering cyclists’ street visual preferences. Detailed analysis indicates the complex relationships between cyclists’ visual preferences and street elements. Our proposed framework not only advances the understanding of individual cycling behaviors but also provides actionable insights for urban planners to design bicycle-friendly streetscapes that prioritize cyclists’ preferences and safety.

## Concept Clarification
**`Cyclists' Route Choice`** A continuous road selection procedure, constrained by origin and destination (OD) and influenced by the built environment, represents how cyclists navigate from place to place.

**`Cyclists' Preferences`** General patterns identified from individual route choice process.

## Research Topic
- How to discover cyclists' prefernces from their routing process?  

- More specifically, we aim to discover cyclists’ general **street visual preferences** based on their continuous route decision procedures influenced by streetscape characteristics.

## Our Solution
we propose an **Inverse Reinforcement Learning(IRL) based framework** to **quantify** and **interpret** cyclists' visual preferences along urban streets, focusing specifically on their cycling process. The overall research idea is described as follows. 

- **Data**: Dockless-Bike-Sharing(DBS) Trajectory Data & Street View Imagery(SVIs) 
- **Methodology**: Maximum Entropy Deep Inverse Reinforcement Learning(MEDIRL) ＋ Explainable Artificial Intelligence(XAI)  

<p align="center">
  <img src="https://github.com/user-attachments/assets/19a350ce-f5fa-4df5-b349-cb7d895330ab"  title="Figure 1. Research Conceptual Framework" />
  <br />
  <em>Figure 1. Research Conceptual Framework</em>
</p>

  
### Fitness of reseach question and methodology
- IRL is effective in mining sequential dependencies and semantic information in trajectory data.
- IRL is flexible in integrating Deep Learning(DL) architectures and high dimensional features, which helps capture thenon-linear and complicated nature of cycling preferences.
- The unique training process of IRL makes it more behaviorally interpretable compared to conventional DL methods and facilitates further simulation and optimization.  

### Framework
The overall workflow comprises three distinct steps, as illustrated in **Figure 2**. Practically, cycling is treated as a route decision process constrained by road spatial networks, taking into account origin-destination (OD) pairs and street visual environments. 

- Formalize cycling process as a Markov Decision Process (MDP) by integrating SVIs and DBS trajectories to **detail cycling procedures outlined earlier** for further analysis.
- Employ IRL to **recover the underlying reward function of MDP from observed trajectory data**. The reward function reflects the general principal cyclists follow, influenced by environmental factors, and served as quantified street visual preferences.
   - Approximate this reward function using a combination of maximum entropy model and deep neural network (DNN) to balance diverse cyclist preferences and capture their non-linear nature (MEDIRL). 
   - Validate learned results by comparing similarities between reconstructed and real trajectories.
-  Utilize XAI to **interpret the contributions** of specific visual elements to cyclists' street visual preferences.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/e83100dc-7758-4f08-b447-a266d79c6dda"  title="Figure 2. Overall Workflow" />
  <br />
  <em>Figure 2. Overall Workflow</em>
</p>

## Partial Results of Our study
### Desciptive Statistics of Model Output
#### Model Settings
- **Quantify cyclists’ general street visual preferences** by training the MEDIRL model in Bantian Sub-district in Longgang District, Shenzhen.
- Model cyclying process as an MDP with a 100m grid size and a 0.99 discount rate.
- Approximate the relationship between state features and the reward function utilizing an Multi-Layer Perceptron (MLP) with 4 hidden layers and Rectified Linear Units (ReLU). Notably, **the value of reward function at each state represents quantified cycling preferences**.
- Discover the spatial dependence and spill-over effects of cyclists' preferences by utilizing Local Indicators of Spatial Association (LISA).
    
#### Model Result
- Spatial distribution of normalized cycling preferences.
- Spatial clustering of normalized cycling preferences.
    
<table align="center" width="100%">
  <tr>
    <td><img src="https://github.com/user-attachments/assets/14d4fda5-8b67-4c46-8bff-83952108d90e" width="500" alt="Figure 3" /></td>
    <td><img src="https://github.com/user-attachments/assets/c0437627-a85a-485c-af7d-56efe4aa7808" width="500" alt="Figure 4" /></td>
  </tr>
  <tr align="center">
    <td><em>Figure 3. Spatial Distribution of Normalized Reward</em></td>
    <td><em>Figure 4. Spatial Clustering of Normalized Reward</em></td>
  </tr>
</table>

### Model Evaluation
#### Model Settings
- Employ agent-based model where the output of trained MEDIRL model serves as behavioral rules to generate new trajectories.
- Measure the **similarity between the state occurrence frequencies** in two trajectories using **Jensen-Shannon Divergence(JSD)**.
- Assess the **similarity between individual trajectories** utilzing **Common Part of Commuters(CPC)**.
  
#### Model Results
- Statistical similarity between actual and synthetic trajectories.
- Similarity between actual and synthetic trajectories at the individual level.

<table align="center" width="100%">
  <tr>
    <td ><img src="https://github.com/user-attachments/assets/9c0c3ce0-f77f-482d-b53c-5e7d0e8a30e7" width="1000" alt="Figure 5" /></td>
  </tr>
  <tr align="center">
    <td><em>Figure 5. SVF Distributions of Real and Synthetic Trajectories</em></td>
  </tr>
</table>

<table align="center" width="100%">
  <tr>
    <td ><img src="https://github.com/user-attachments/assets/a906abf4-42f0-4dc2-88db-588da60b33e8" width="250" /></td>
    <td ><img src="https://github.com/user-attachments/assets/d4d0b14b-8591-4209-8fcb-3eb140efd66a" width="250" /></td>
    <td ><img src="https://github.com/user-attachments/assets/8dcbbf29-9a9f-423c-a24a-b635fac3156b" width="250" /></td>
    <td ><img src="https://github.com/user-attachments/assets/b3443228-44a1-4825-8b0c-33e2cacfc490" width="250" /></td>
  </tr> 
</table>

<p align="center">
  <em>Figure 6. Selected Trajectories and Corresponding Generated Data</em>
</p>

### Interpretability of Environmental Preference of Route Decision Process
#### Importance of the Street Visual Elements

<table align="center">
  <tr>
    <td ><img src="https://github.com/user-attachments/assets/8e78ee2d-016c-47d5-bde3-b60c11eb08b9" width="500" alt="Figure 7" /></td>
    <td><img src="https://github.com/user-attachments/assets/25bd3432-4859-4349-a983-0338ff5a276e" width="560" alt="Figure 8" /></td>
  </tr>
  <tr align="center">
    <td><em>Figure 7. Feature SHAP Value of Each Sample</em></td>
    <td><em>Figure 8. Average SHAP Value of Each Feature</em></td>
  </tr>
</table>

#### Nonlinear and Threshold Effect of Each Street Visual Elements on Cycling Reward
  
<table align="center" width="100%">
  <tr>
    <td ><img src="https://github.com/user-attachments/assets/0909ee47-762c-4f49-94b1-98ceb58de5a0" width="500" alt="Figure 9" /></td>
    <td><img src="https://github.com/user-attachments/assets/d8292243-153d-4ad4-80c6-c655bf5e831a" width="510" alt="Figure 10" /></td>
    <td><img src="https://github.com/user-attachments/assets/eceaa21a-5aff-4718-b5e3-944a4b115826" width="500" alt="Figure 11" /></td>
  </tr>
  <tr align="center">
    <td><em>Figure 9. Green View Index SHAP</em></td>
    <td><em>Figure 10. Sky View Factor SHAP</em></td>
    <td><em>Figure 11. Motorcycle SHAP</em></td>
  </tr>
</table>

#### Interactions Between Key Street Visual Elements

<table align="center" width="100%">
  <tr>
    <td ><img src="https://github.com/user-attachments/assets/cde6f2c9-4cf3-4a49-9bcc-e8b1c9ccf11e" width="500" alt="Figure 12" /></td>
    <td><img src="https://github.com/user-attachments/assets/60f84dff-a9c7-4caa-971e-d506f89ac1cf" width="500" alt="Figure 13" /></td>
    <td><img src="https://github.com/user-attachments/assets/775b32cd-bd7c-4e90-b51b-8cc14cc286d0" width="500" alt="Figure 14" /></td>
  </tr>
  <tr align="center">
    <td><em>Figure 12. Interaction between GVI & Wall</em></td>
    <td><em>Figure 13. Interaction between Motorcycle & SVF</em></td>
    <td><em>Figure 14. Interaction between Motorcycle & Wall</em></td>
  </tr>
</table>


# Part 2. Documentation

## Algorithms Implemented
- Linear programming IRL. From Ng & Russell, 2000. Small state space and large state space linear programming IRL.
- Maximum entropy IRL. From Ziebart et al., 2008.
- Deep maximum entropy IRL. From Wulfmeier et al., 2015; original derivation.
- [Inverse-Reinforcement-Learning From Mattew Alger et al., 2017.](https://github.com/MatthewJA/Inverse-Reinforcement-Learning?tab=readme-ov-file)

A Data-Driven Framework For Discovering Cyclists' Street Visual Preferences Through Multi-Source Big Data -> **Problem Oriented**

Cycling Procedure MEDIRL e-> **Technological Oriented**


## Introduction: importance of cycling and DBS system 
Cycling, widely recognized as a sustainable means of transportation, promotes outdoor activities and presents a potential solution to urban challenges such as traffic congestion and air pollution. The emergence of Dockless Bike Sharing (DBS) has further enhanced cycling by significantly improving accessibility to active travel. Consequently, DBS has garnered widespread adoption across numerous countries and has surged in popularity, particularly following the Covid-19 pandemic. Unlike motor vehicle travel, cyclists make decisions based not only on long-term travel plans but also on immediate environmental factors. However, urban planning often fails to accommodate the unique characteristics of cycling behavior, resulting in insufficient support for cyclists. Therefore, gaining a detailed understanding of cyclists' preferences and behaviors within DBS systems is crucial for bicycle-friendly urban planning.     **->Background**

The integration of GPS devices in DBS systems generates valueable location-based data, sparking significant academic interest in the fields of transportation and urban planning. Researchers have diligently studied cyclists' behavior and its correlation with various environments using data driven approaches. However, existing studies often prioritize analyzing cyclists' Origins and Destinations (ODs) rather than examining the detailed cycling procedures. This oversight may limit urban planners' understanding of how cyclists' behaviors relate to their on-site environments, which are crucial for understanding environmental preferences and influencing the scientific design of urban streets. To tackle the oversight of cyclists' preferences regarding their surroundings during DBS cycling, we have identified two key challenges.    **The importance of cycling procedure**

**The primary challenge lies in comprehensively understanding and describing the detailed procedures of cycling**. One of the most common and intuitive methods is Route Choice Modeling(RCM), which predicts the possible paths that individuals follow during their trips. Typically, the principles uncovered in route selection are often interpreted as cycling preferences. The RCM framework is highly regarded for its potential and effectiveness in integrating new data and methodologies. Some studies integrate DBS trajectory data into RCM, treating cycling volume as a proxy for subjective preferences. However, DBS volume, affected by supply, demand, and temporal patterns, maks it difficult to accurately infer cyclists’ preferences from aggregated data. Some researchers have combined Agent-Based Model (ABM) with RCM to simulate real-time interactions from cyclists’ perspective. Yet, the development of such studies often rely on pre-defined indices and behavioral rules,  potentially overlooking implicit information in cyclists' decision-making processes. In other domains like ridesharing, deep learning methods like LSTM and GRU capture spatiotemporal dependencies in trajectories. However, cyclists, who both use and navigate the environment, exhibit different decision-making patterns compared to taxi passengers. Thus, understanding individual cycling processes is crucial for data-driven approaches to uncover cyclists' preferences.

**Another challenge followed immediately is to capture and uncover cyclists' environmental preferences in cycling procedures.** Traditionally, traffic surveys are employed to explore the relationship between cycling behavior and macro-level Built Environment (BE) factors like infrastructure and land use. Yet, they often overlook preferences for various micro-level Street Environment (SE) visual features, limiting practical applications in urban planning. Moreover, existing studies frequently assume linear utility functions, which fail to adequately capture the complex and nonlinear routing decisions influenced by environmental factors. The emergence of multisource big data and Artificial Intelligence (AI) offers new opportunities to accurately capture cyclists' experiences in urban environments. Street View Images (SVI) and DBS trajectory data allow for a human-centric characterization of cyclists' routing decisions, with AI advancements extracting intricate preferences from diverse data sources. However, deep learning methods often lack explanatory, resulting in limited applicability in urban planning. In summary, these data-driven technological advances pave the way for a cognitively interpretable model framework to uncover cyclists' environmental preferences from their cycling procedures.

There are two gaps in the data-driven research on the cyclists' preferences for street environments. The first is how to understand cycling procedures while considering the impact of SE. The second lies on how to extract coherent cycling preferences towards SE from highly random and heterogeneous big data.

In recent years, reinforcement learning(RL) has shown excellent ability in dealing with sequential decision-making problems in random situations (Li, 2023; Qin et al., 2022), and has been widely adopted in trajectory data mining, route recommendation, vehicle repositioning and other researches. However, RL methods often rely on predefined operating rules (Rong et al., 2016; Yu et al., 2019; Yu & Gao, 2022), while the Inverse Reinforcement Learning(IRL) reverses the above process and recovers the principles that the agent potentially follows from the cycling information through the combination of simulation and training(Abbeel & Ng, 2004; Ng & Russell, 2000), which provides an opportunity for researchers to measure cycling procedures and reveal the complex cyclists' environmental preferences from given data.

To build upon existing research and bridge identified gaps, we propose a framework that integrates multi-source big data and IRL to quantify and interpret the preferences in the route choice process. Specifically, we take Bantian Community, Longgang District, Shenzhen as the empirical research area, and on the basis of reconstructing the route decision-making process of cyclists, we integrate data such as DBS trajectories and street view images (SVI), and employ the maximum entropy deep inverse reinforcement learning (MEDIRL) method to automatically reveal the position preference from the perspective of cyclists. To verify the method's effectiveness, we simulate trajectories based on the extracted position preferences, and assess the similarities between these simulated trajectories and the real trajectories. Finally, we adopt explainable artificial intelligence (XAI) techniques to illustrate the complex relationship between cyclists' real-time perception and route decisions.
The major contributions of this study can be concluded in three aspects:

 1. We proposed a comprehensive framework for unraveling the cycling preference of urban streets, emphasizing a detailed process that goes beyond conventional OD analysis. DBS trajectories offer insights into the entire cycling process, enabling a more nuanced understanding of cycling route decision, while SVI provides opportunities to accurately describe street-level visual features related to cycling trips.
     
 2. Our study proposed a novel cycling preference quantification and interpretation method, leveraging results derived from MEDIRL and XAI models. This method automatically establishes a robust link between the street environment and cycling behavior, explicitly considering their complex interactions. Compared to existing methods, our data-driven method offers enhanced reliability and reasonability.
    
 3. We applied our proposed framework in a real-world scenario, specifically in Ban Tian community in Longgang District, Shenzhen. The quantification and interpretation of cyclists’ preferences were conducted by considering both path-level (i.e., OD) and link-level characteristic for each trajectory. The practical case study underscores the feasibility and reliability of our proposed method.

The rest of the paper is organized as follows. Section 2 introduces the study area and dataset. Section 3 outlines our methodological framework, including maximum entropy deep inverse reinforcement learning, explainable artificial intelligence, and the metrics we utilized. In section 4, we conduct an empirical research in study area to validate the reliability and explainability of our approach. Section 5 summarizes this research and outlines the future work.


## Study Area and Dataset
### Study area
In our study, we focus on Bantian Sub-district in Longgang District, Shenzhen as the research area. This area is characterized by relatively consistent cycling demand, convenient traffic facilities, comfortable travel conditions and diverse environmental attributes, making is suitable for investigating cyclists' preferces to environmental elements.

Bantian Sub-district has served as a showcase for the integration of technology and urban development within the Guangdong-Hong Kong-Macao Greater Bay Area. It is particularly renowned for its technology industry, and attracts a large number of young commuters. Situated on the border of three districts in Shenzhen, the area offers diverse transportation options for residents. Specifically, it boasts well-established public transportation, including 2 metro lines with 22 subway stations, complemented by a sufficient supply of DBS services. The total road network spans 38.97 km, comprising 5,229 intersections and 7,039 road segments accessible to cyclists. Moreover, Bantian Sub-district provides favorable conditions for year-round outdoor cycling with an average temperature of 23.3°C and gentle slopes averaging less than 10°. Its spatial heterogeneity in natural and socio-economic environments enables us to distinguish between various areas and extract typical attributes.
  
### Data
#### DBS Trajectory Data
The DBS trajectory data utilized in this study were sourced from a well-known DBS service provider, comprising **10,00** independent trips collected in Bantian Sub-district from Nov 1st to Nov 30 th, 2017. Specifically, our DBS trajectory data encompass basic order details such as Order ID,  User ID, DBS ID, Start Time, End Time, Start Coordinate, End Coordinate and a sequence of trajectory points collected at three-second interval, as illustrated in Table 1. Preproccessing of DBS trajectory data involves three stages: raw data cleaning, map matching and data filtering.

First of all, we identified and eliminated the counter-intuitive cycling trips in order to enhance data quility. Specifically, we filtered out trips less than three minutes or exceeding one hour, considering the rebalancing process. Additionally, we removed the trajectory points where speeds exceeded 30 km/h, likely due to poor GPS signal. Following this data cleaning process, we obtained a dataset of **10,000** distinct cycling trips suitable for map matching.

Second, we mapped trajectory points onto the road network using a Hidden Markov Model(HMM) to better approximate the link-based decision-making process of DBS cycling. This method successfully assigned a sequence of road segments to the trajectory points. Furthermore, to validate the effectiveness of map-matching process, we randomly selected several mapped trajectories and compared them with raw data. As shown in **Figure 1**, this comparison demonstrated convincing result.

Finally, we filtered the mapped DBS trajectory data using specific criteria informed by preliminary literature reviews and exploratory analysis. Given the subtropical location and an average November temperature of 19.7℃, our data comprehensively represented cycling behavior. To account for the direct impact of weather conditions on cycling, we excluded data from two rainy days(Nov 9th and Nov 16th). Additionally, to mitigate potential biases in estimating preferences due to temporal changes, we focused our analysis on cyclists' behaviors during weekdays and daylight hours. Furthermore, our DBS trajectories deviated significantly from the shortest path when applying the Dijkstra Algorithm, aligning with findings in current literature. Specifically, approximately 83.8% of cyclists selected the shortest path for trips involving fewer than five road segments. Therefore, we concentrated on cycling trips with more than five road segments, resulting in **10000** distinct trip trajectories as the valid dataset for further investigation. The results of exploratory data analysis are shown in **Appendix**.

#### Street View Images
Street View Images (SVI), a widely used type of big geospatial data, offers detailed visual representations of urban physical environments. Additionally, SVI implicitly capture invisible information like socio-economic environments and human activities. In our research, SVI remains largely unchanged due to the subtropical climate, making it suitable for simulating cyclists' real-time visual perceptions on urban streets.

The SVI data used in this study were obtained from Baidu, comprising 7924 distinct panoramas in Bantian Sub-district, primarily captured in 2017. Semantic segmentation was conducted using the DeepLabV3+ model pretrained on the Cityscapes dataset, to extract visual elements. As a result, we identified eight primary categories and 21 detailed subcategories of street scenery, as detailed in Table 2. Subsequently, we quantified the cyclists' visual perceptions by calculating the ratios of the pixels assigned to each category relative to the total number of pixels in the image, normalized using min-max scaling between zero and one. The segmentation achieved an average coverage of 97.88%, indicating its applicability for further investigation.

## Methodology
### Framework
The detailed procedure of cycling  involves abundant temporal and semantic information, providing researchers with insights to cyclists' behavioral patterns. However, the complexity of cycling environments and the stochastic nature of behaviors present challenges in uncovering cyclists' preferences from  detailed procedures.

In our study, we propose a data-driven framework designed to quantify and interpret cyclists' visual preferences along urban streets, focusing specifically on their cycling procedures. The overall workflow comprises three distinct steps, as illustrated in **Fig 1**. cycling is treated as a route decision process constrained by road spatial networks, taking into account origin-destination (OD) pairs and street visual environments. We formalize it as a Markov Decision Process (MDP) integrating SVI and DBS trajectories. Secondly, we employ Maximum Entropy Deep Reinforcement Learning (MEDIRL) to quantify cyclists’ environmental preferences derived from the cycling procedures outlined earlier. We validate learned results by comparing similarities between reconstructed and real trajectories. Finally, we utilize explainable Artificial Intelligence(XAI) to interpret the contributions of specific visual elements to cyclists' environmental preferences.



### Preliminaries and Problem Formulation
Cycling procedures can be regarded as a MDP, which provides a general framework for modeling the sequential decision process of a cyclist. A MDP is generally defined as $M=\{S,A,T,R,γ\}$, where $S$ denotes the state space, representing the set of possible positions the agent can be; A denotes the set of possible actions the agent can take. Generally speaking, the sequence of state-action pairs is also referred to as the trajectory, i.e., \{(s_1,a_1 ),(s_2,a_2 ),···,(s_t,a_t )\}. T(s_t,a_t,s_(t+1) ) denotes a transition model that determines the next state s_(t+1) given the current state s_t and action a_t. R(s,a) is the reward function, defined as the feedback obtained by the agent when taking action a∈A in state s∈S. In the modeling of sequential decision-making problems, the policy π describes the moving strategy at each stat. The agent's policy is often non-deterministic, and this stochastic policy can be intuitively understood as the probability of the agent taking action a_t∈A given the current state s_t∈S, denoted as Pr(a_t│s_t ). The quality of a policy is often evaluated based on its long-term return, and the most popular definition is the discounted return, i.e., G_t= ∑_(i=0)^(+∞)▒〖γ^i r_(t+1) 〗  γ∈[0,1]. When γ=0, the agent is short-sighted, only focusing on immediate rewards and disregarding the temporal dependencies of the policy; as γ approaches 1, the agent considers future rewards more. In the RL setting, the reward function R(s,a)  s∈S,a∈A is given, and the objective is to find the optimal policy π^* that maximizes the expected cumulative reward for the agent. This is accomplished by sampling trajectory data through continuous interaction between the agent and the environment.
In our study, cyclists are treated as agents in an MDP. Solving this MDP model will give us the optimal decision strategy for each different location. Specifically, we can define the elements of the MDP as follows: 
 
- **State**: Each state s∈S is a vector used to describe the basis of a cyclist’s decision-making. Due to the simulation-based learning of cyclists behavioral rules under the given ODs, the agent cannot obtain specific path information beforehand. Therefore, in our study, each state is a link in road network indicating the current location and corresponding perceptions of the cyclist, denoted as s=\{Dest,Pos,BE\}. The vector Dest is the final state of current agent. The vector Pos is utilized to represented the links and the 100m grid units where agent is located, serving as the core determinants of its location. Depending on data availability, the real-time perception of the cyclist can be incorporated, but is outside the scope of this study. Alternatively, we will regard SVI as great approximation of cyclist’s perception, following most prior works(Zhang et al., 2018). As a result, the vector BE is composed of the semantic elements of SVI. (The relationship between SVI & perception)
- **Action**: An action a∈A indicates the grid-to-grid movement choice under the restriction of road networks. Liang & Zhao (2022) has shown that a directional representation can yield better route prediction performance, as a result, we define a global action space A consisting of 9 movement directions — forward (F), forward left (FL), left (L), backward left (BL), backward (B), backward right (BR), right (R), forward right (FR), and stay(ST), as shown in Figure.7. Note that, although these 9 directions represent a comprehensive set of all potential actions to be taken anywhere, only a subset of them are applicable for most states. In order to account for the specific layout of the local network, we have also defined a local action space A_s∈A to capture all valid actions at each state s. 
- **Policy**: Generally, a policy, denoted as π(a|s), dictates the actions an agent takes in each state s∈S. These policies can vary, guiding agents to select different actions even in similar states, resulting in diverse trajectories. In our study, the policy describes how cyclists make route decisions, namely the process of selecting links under the influence of the built environment. The optimal policy, denoted as π^*, represents the most representative route decision-making pattern for cyclists.
- **Reward function**: The reward function R(s,a) characterizes cyclists' preferences for the built environment in the route decision-making process. Corresponding to the optimal policy π^*, R^* represents the reward function that best explains cyclists' route preferences. Additionally, in this study, a set of parameters θ is used to fit the utility function of cyclists interacting with complex and heterogeneous environments, thereby replacing the location-based reward representation method to store the mapping between states, actions, and their rewards, denoted as R_θ (s,a)=θ(Pos,BE,dest). As mentioned earlier, the rewards dictate the actions of the agent. Therefore, compared to the agent's policy, the reward function R is more likely to provide researchers with insights into its decision-making mechanism.

In summary, our study models the cycling procedure as an MDP. It can be described as the process where cyclists make continuous decisions about street selection based on their immediate perceptions, aiming to maximize their cumulative return. However, it is often difficult to characterize the relationship between cyclists' immediate perceptions and their decision-making tendencies using a predefined reward function, which significantly restricts the applicability of such approaches. Fortunately,  Andrew Ng's framework of Inverse Reinforcement Learning (IRL) (Abbeel & Ng, 2004; Ng & Russell, 2000) offers a solution. By reversing the RL process, IRL extracts the reward function from demonstrated data. This methodological approach provides a solid foundation for addressing the challenges mentioned earlier.

## Experiments
To quantify the cyclists' environmental preferences, we evaluate our proposed MEDIRL model by comparing actual and predicted route choices. The prediction resembles an agent-based simulation where the output of trained MEDIRL model serves as behavioral rules to generate new trajectories. Subsequently, we evaluate similarity between synthetic and real trajectories based on statistical and route characteristics. 

Furthermore, to interpret the proposed model, we employ the SHAP algorithm to examine the contribution of each street visual element within each unit, thereby assessing the importance of each feature and their complex relationships in cyclists' preferences thatwe extracted before.

### Model output
We train the MEDIRL model on integrated SVI and DBS trajectories to automatically extract cyclists' environmental preferences. Specifically, our approach employ a Multi-Layer Perceptron (MLP) with 4 hidden layers and rectified linear units (RELU) to approximate the relationship between state feature representations and rewards. We plot the spatial disrtibution of cycling reward for each state in **Figure 1**. Globally, Biantian Sub-district exhibits a mean cycling reward of 0.40 with a variance of 0.12. Specifically, the overall distribution in this area shows a right-skewed pattern where the mode of cycling rewards is less than its mean. This indicates that Biantian Sub-district has many locations with relatively low cycling rewards, suggesting distinct preferences in riders' choices.

We also visualize the spatial distribution of quantified cyclists' preferences, as shown in Figure 2-X. The varying shades of basic study units represent the degree of preference that cyclists have for corresponding locations. From the figure, it is evident that cyclists exhibit significant spatial clustering in their location preferences. 

To quantify the spatial dependence of cyclists' preferences, we first models the target variables using a Fixed Distance Band to conceptualize spatial relationships. To determine the optimal critical distance, we employ the Incremental Spatial Autocorrelation Tool, which uses Z-Scores to identify distances that most clearly promote spatial clustering processes. The results indicate that the first peak Z-Score corresponds to a critical distance of 228.95 meters. Thus, this distance is chosen as the threshold for conceptualizing spatial relationships in the model. At this critical distance, the Z-Score is 65.12 and Moran’s I value is 0.42, passing a statistical test significant at the 0.001 level, demonstrating a significant spatial autocorrelation in riding rewards and a clear overall clustering phenomenon.

Furthermore, to identify the locations and boundaries of riding reward clusters, we utilize hotspot analysis, employing the Getis-Ord Gi* index to measure local spatial autocorrelation of cycling rewards. It identifies high and low-value clustering areas within communities, as depicted in **Figure b)**. Overall, we identify 13 high-value clustering areas and 15 low-value clustering areas within the Biantian Sub-district. High-value clustering areas are typically located within the community and exhibit decreasing autocorrelation strength as distance increases. In contrast, low-value clustering areas tend to appear at the boundaries between communities.

<p float="left">
  <img src="https://github.com/user-attachments/assets/14d4fda5-8b67-4c46-8bff-83952108d90e" width="45%" />
  <img src="https://github.com/user-attachments/assets/c0437627-a85a-485c-af7d-56efe4aa7808" width="45%" /> 
</p>

### Model Evaluation
Following established methods in the field, we evaluate our model by comparing the similarity between actual cyclists' trajectories and synthetic data generated using the learned preferences. We initially measure the similarity between real and synthetic trajectories based on their statistical characteristics as summarized in Fig.9. In our dataset, the calculated JSD between the distributions is 0.3484, indicating a significant degree of resemblance between the synthetic and real trajectories in terms of fluctuation ranges. However, we observed that the synthetic trajectories exhibit higher means and smaller variances compared to the real trajectories. This suggests that further refinement of the reward function is necessary to better capture the characteristics of longer trips. 

Moreover, we utilize the Sørensen-Dice coefficient to evaluate the similarity between individual trajectories. The probability density function is illustrated in **Figure.10 (a)**. Our findings reveal that, on average, synthetic trajectories overlap with real ones by 66.67% for each OD pair. Our descriptive statistical analysis, as shown in **Figure 10**, provides deeper insights into their similarity based on decision frequency. Our results highlight that trajectories generated under learned reward excel in reflecting preferences for medium to short-distance cycling paths. Employing the elbow method to analyze the relationship between decision frequency and CPC, we observed that that once the number of decisions exceeds 18 in a single trip, the rapid decline in similarity between trajectories halts. 

To gain more intuition about model outputs,  we also visualize an example of a real trajectory from the data and its corresponding synthetic trajectory generated by our model, shown in **Figure 4** as a comparison. The results indicate that our link-based MEDIRL model effectively captures cyclists' sequential decision-making patterns from real trajectory data.

### Interpretability of Environmental Preference of Route Decision Process
The preferences of cyclists towards street visual elements are complex, and identifying dominant factors can provide evidence for streetscape design interventions to ehance the cycling experience. In this paper, we explain the output of MEDIRL by estimating the marginal contribution of each features within different research units utilizing SHAP algorithm, which provides deeper insights into the decision-making process of our proposed model.

#### Relative Importance of the Street Visual Elements
From a global perspective, we rank importance of factors based on the reward network of MEDIRL. We display the distribution of SHAP values for street-level environmental elements of different states in Figure X. Various visual elements show noteworthy disparities in their influence on cyclisting reward, contributing a lot to cyclists' preferences. In terms of total impact, it is apparent that the average SHAP value of the proportion of motor vehicles in SVI is much higher than the other features. Another factor that influences cycling behavior is the perceived road network density. Following closely in contribution are several categories of street visual elements, including building facade proportion, Sky View Ratio(SVR), proportion of fences, Green Giew Index(GVI), and proportion of terrain elements. 

It is found that cyclists' focus on street visual elements can be simplified into four main needs: right of way, likelihood of route selection, sense of safety, and comfort while cycling. Specifically, cyclists are particularly sensitive to sharing lanes with other modes of transportation. As an indicator of their concern for right of way, low proportion of motor vehicles is assigned with a positive SHAP value, suggesting motor vehicles in their visual field negatively affects their preferences. To put it differently, cyclists tend to choose routes with fewer motor vehicles, reflecting their emphasis on right of way. Simiarly, road density perceived by cyclists at their current location has a negative impact on their preferences, aligning with findings on drivers' route decision aversions to complex intersections. Elements such as building facades, urban greenery, and fences reflect cyclists' sense of safety, influencing route choices by enhancing traffic calming and enclosure perceptions. Cyclists also show a preference for routes with higher Green View Index (GVI) for comfort, while routes with higher Sky View Ratio (SVR) are less favored, indicating a prioritization of shaded areas over open skies, particularly significant in subtropical areas.

<p float="left">
  <img src="https://github.com/user-attachments/assets/8e78ee2d-016c-47d5-bde3-b60c11eb08b9" width="45%" height="100%" />
  <img src="https://github.com/user-attachments/assets/25bd3432-4859-4349-a983-0338ff5a276e" width="45%" height=100% /> 
</p>

#### The Nonlinear and Threshold Effect of Each Street Visual Elements on Cycling Reward

The preceding discussion underscores the diverse impacts of street visual elements on cycling decisions, revealing their multifaceted contributions to cyclists' preferences. Meanwhile, each type of element serves multiple needs: for instance, the Green View Index (GVI) not only measures shading, enhancing cycling comfort, but also signifies enclosure. Similarly, building facade proportions influence perceptions of safety and contribute to street design continuity. These multidimensional implications suggest nonlinear relationships between environmental factors and cycling route decisions. To explore this further, we identified six elements of high global importance based on expected SHAP values. Without considering potential variable interactions, we drew their local dependency plots on cycling rewards in **Figure X**. These plots illustrate how changes in each element affect cycling preferences: higher y-axis values indicate greater impact, while steeper slopes indicate heightened sensitivity to those changes.

The findings presented in **Figure 15** demonstrate that the selected street visual elements do not fit into simple categories of positive or negative impacts. Instead, their effects vary depending on their proportions.

Specifically, the proportion of motor vehicles has a contribution to cyclists' route choices that initially promotes and then inhibits, with their marginal effects showing a roughly four-stage pattern: Cyclists tend to favor links with less traffic volume and steer clear of those with higher traffic volume. In addition, within the standardized range of 1.5-2.0, cyclists are highly sensitive to changes in the number of motor vehicles.

The contribution of building facades and fences to cycling preferences exhibits distinct two-stage trends, both in terms of their impact and marginal effects. Building facade proportions show a negative SHAP value when standardized measures are below 0.5, indicating cyclists tend to avoid streets with minimal enclosure. However, this trend reverses around and beyond a value of 1, with a diminishing marginal effect, suggesting a threshold where increased facade proportions do not significantly enhance cycling rewards.Conversely, the proportion of fences initially positively impacts cycling preferences, stabilizing with a plateaued standardized SHAP value around 2. This suggests that the presence or absence of fences, rather than their quantity, markedly influences cyclists' route choices. 

The contribution of SVR related to street comfort to cycling preference exhibits a characteristic of initial promotion and then inhibition, and its SHAP value also shows a similar two-stage feature. After standardization, the SVR starts to have a stronger inhibitory effect on cycling rewards. In contrast, the GVI demonstrates an opposite trend in its contribution to cycling preference compared to the SVR. Precisely, cyclists' sensitivity to GVI in the range of 0-2 is roughly similar. As the standardized GVI increases to 3, the change in SHAP values gradually approaches stability, and even in some streets, the marginal effect of SHAP values decreases. The reason for the phenomenon is that excessively high GVI may be related to a lack of necessary public service facilities and functions. Additionally, the contribution of terrain elements to the change in cycling preference displays a trend of an inverted U-shape, promoting first and then inhibiting. It can be seen from the graph that the effect of terrain elements is highest when it accounts for approximately 8%.

In summary, visual environmental elements exhibit complex relationships with cycling behaviors, often demonstrating threshold effects. Specifically, changes in the proportion of motor vehicles illustrate a nonlinear impact on cyclist preferences regarding right of way. Visual elements that enhance safety perceptions—such as building facade proportions, fencing, and GVI—and those improving comfort, like SVR, show marginal effects of their SHAP values gradually decreasing and eventually converging. Therefore, strategically managing the proportions of visual elements on streets is crucial for influencing cyclists' route choices, promoting cycling activities, and encouraging favorable cycling behaviors.

#### Interactions Between Key Street Visual Elements
To uncover the potential impact of interaction effects between visual environmental variables on cycling preferences, we computed the SHAP Interaction Value for each variable pair. **Figure 16** presents a heatmap illustrating the average strength of these interactions across our samples. From this analysis, we identified three pairs of variables with the strongest interaction effects, which are further explored in Figure 17 through partial dependence plots. In these plots, the X-axis represents the target variable, while color indicates the magnitude of values from another independent variable involved in the interaction. The Y-axis represents the SHAP interaction values quantifying the relationship between the two variables.

As a critical factor influencing cyclists' route decisions, there exists a strong interaction between cyclists' attention to road rights and various visual elements of streets. Firstly, an interaction is noted between the proportion of motor vehicles and the proportion of building façades in the streetscape. This interaction exhibits a threshold effect: when the proportion of motor vehicles is low, the SHAP interaction value increases with an increase in the proportion of building facades. In other words, within this threshold range, street enclosure is the primary consideration for cyclists' route decisions. However, as the number of motor vehicles increases, the SHAP interaction value gradually decreases. When it reaches around zero, cyclists shift their attention more towards road rights. Therefore, for roads with high traffic volumes, promoting cycling activities by enhancing street enclosure through building construction is not advisable; instead, it may instead exert a suppressive effect on cycling.

Similarly, there is a strong interaction between cyclists' attention to road rights and the comfort of cycling, particularly manifested in the interaction between the proportion of motor vehicles and the SVR. There is also a noticeable threshold effect as illustrated in **Figure (c)**. When the number of motor vehicles is low, higher SVR values correspond to higher SHAP interaction values, suggesting that cyclists are encouraged to choose these routes at this time. However, as the number of motor vehicles increases, the contribution of SVR to cyclists' route preferences reverses, indicating a reluctance to choose links with relatively high SVR. This phenomenon suggests that the intervention on SVR and traffic calming may affect the average cycling levels on targeted segments.

There is also an interactive effect between indicators representing cycling safety and comfort. In this study, we take the proportion of building facades and the GVI as examples. As shown in Figure (e), streets with a low proportion of building facades and a high GVI significantly contribute to a positive cycling preference. In such scenarios, enhancing the GVI through design measures has high marginal utility, effectively promoting cycling activities. Conversely, streets with a high proportion of building facades and a low GVI only weakly contribute to cycling decisions. Hence, we infer that GVI has a slightly greater influence on cycling preference than the level of enclosure measured by proportions of buildings. Consequently, a balanced combination of natural elements and artificial built environment features positively enhances the cycling experience, whereas an imbalance may lead to suboptimal outcomes.

## Conclusion and Discussion
### Conclusion
Our study proposes a framework for unraveling environmental preferences in context of route decision processes. Specifically, we formulate the cycling process as a MDP. Based on utilizing MEDIRL to quantify cyclist link-based preference from DBS trajectory data, we employ XAI techniques to discern the impact of urban environment on cycling behavior, revealing cyclist principle of decision under the influence of real-time perception. 

The results indicate that, firstly, the MEDIRL can effectively infer the underlying reward function of cycling process, and the synthetic trajectories guided by learned reward can well replicate the statistical and path characteristics of actual trajectories. Secondly, by further exploring the learned cyclist preferences, this study finds that cyclists are most concerned about the right of way for bicycles and tend to prefer links with high enclosure, comfortable environment, and strong decision continuity. Lastly, our study reveals nonlinear interaction between cyclist decision-making and real-time perception: reasonable traffic calm measures and appropriate combination of artificial and natural elements contribute to an increased probability of cyclists choosing a certain route, while unreasonable distribution of visual elements may lead to diminishing or negative marginal effects on cycling preferences.

### Limitations and future work
Although this study is highly replicable to other areas to inform how the link-level SE attributes affect cycling behavior, we acknowledge several directions for future improvement concerning (1) data limitation; (2) preference heterogeneity; (3) model generalization; (4) potential application.

Firstly, immediate interactions with SE play only a partial role during cycling. However, this study uses contemporaneous SVI data as a proxy for cyclist real-time perception due to data limitations. Therefore, future research may incorporate real-time factors such as street physical environment and traffic conditions into the design of state space. By combining On-Policy and Off-Policy training methods, it can more accurately measure cyclists' real-time perception and reveal more precise preference information in their route decision-making processes. 

Secondly, cyclists’ preferences are likely influenced by their travel patterns, which highlights the heterogeneity among different cyclists. However, this study regards DBS users as a homogeneous group. Future research may need to employ embedding techniques to learn more efficient representations of trajectory data, integrating semantic features of trajectories into the preference-unraveling framework. This would not only increase the comparability of different trajectory data but also provide theoretical foundations and technical means to explore the similarities and differences in patterns of route decision among different types of cyclists. 

Thirdly, this study only validates the effectiveness of data-driven methods in the Bantian community of Longgang District, Shenzhen. Future research could extend these methods to new study areas, revealing cyclists' SE preferences in link-level decision-making considering its spatial heterogeneity.

Lastly, the research framework adopted in this study has the potential to be extended into an explainable path recommendation and trajectory generation framework. This could offer customized route planning solutions tailored to cyclists' preferences and provide substantial technical support for researchers facing the challenge of data sparsity in urban data analysis scenarios.

## Appendix 
### Time differentiation characteristics of DBS
To explore the differentiation of DBS cycling behaviors across different time periods, we calculated the Manhattan distances for different travel trips. Due to the log-normal distribution characteristics of cycling distances in statistics, we plotted the frequency distribution histogram of the logarithm of cycling distances as shown in **Figure 2-x**. The results indicate that the logarithmic mean of cycling distances on workdays is approximately 2.3, whereas on weekends, the mean logarithm of travel distances is 2.4. Therefore, compared to workdays, cyclists travel longer distances on weekends, and the variance from the distribution curve also shows greater fluctuations in weekend travel distances. Similarly, the logarithmic mean of nighttime cycling distances is 2.0, which rises to 2.3 during the daytime. Thus, compared to daytime, nighttime cyclists travel shorter average distances with greater fluctuations. Overall, these results align with researchers' intuitive understanding of DBS, indicating that cyclists' behavioral patterns exhibit certain differences across time periods.
<p float="left">
  <img src="https://github.com/user-attachments/assets/5653d5bc-6627-4d0e-93e3-ff1c6fd371f3" width="80%" />
</p>


Our study investigated the nuanced characteristics of riding distances at a granular scale. Figure 2-x illustrated the logarithm of DBS travel distances on the x axis against travel time on the y axis. For clarity, we aggregated the number of DBS trips per hour, depicted in the subplot on the right. Overall, as indicated by the red dashed line in the figure, the average logarithmic travel distance was 2.4. Early morning trips often deviated significantly from this average, while daytime trips tended to align more closely. However, around noon, distances diverged further from the mean. Additionally, travel distances in weekend frequently differed from weekday. This data distribution highlighted substantial variations in cyclists' behavior influenced by daily rhythms. Notably, DBS peaked in usage on weekdays from 6:00-9:00 AM and 4:00-8:00 PM. Meanwhile, trips in early norning of weekends were notably fewer. The variability in travel distances followed distinct statistical patterns throughout different times of the day.
<p float="left">
  <img src="https://github.com/user-attachments/assets/11fa2393-efd8-42d1-af69-916b12dd9251" width="80%" />
</p>


### The difference between DBS trajectory and corresponding shortest path
Previous research has shown considerable variation between cyclists' actual route choices and the possible shortest paths. To assess the applicability of these findings in our context, we compared the similarity between the shortest paths and cyclists' actual trajectories. Firstly, we constructed a directed spatial network based on roads in our research area, weighted by segment lengths. Secondly, we  employed the Dijkstra algorithm on this road network to determine the shortest route for each cycling journey. Lastly, by using similarity metrics, our study contrasted the differences and similarities between cyclists' actual route choices and the shortest paths, thereby providing criteria for decision-making in data selection.

Initially, we analyzed the similarity between cycling distance and the frequency of cycling decision-making, depicting their log-transformed frequency distribution histograms in **Figure 2-x**. Regarding cycling distances, as shown in Figure 2-x a), after log transformation, both distributions exhibited varying degrees of left-skewed normal distribution, with more data concentrated to the left of the mean and some extreme values to the right. Specifically, the mean log-transformed actual trajectory cycling distance was 2.9, whereas the mean log-transformed shortest path cycling distance was 2.6. This suggests that cyclists do not strictly follow the shortest path when making route decisions. We also annotated the quartiles of both trajectories, indicating that the fluctuation in cycling distance for actual paths was smaller than that for the shortest path.

Additionally, we plotted the probability mass distribution of cycling decision-making frequencies with a single trip, as depicted in **Figure 2-x b)**. Two peaks were evident around 3 and 8 decisions. This phenomenon indicates that as the number of decision increases during a single trip, cycling behavior shows different trends, highlighting the necessity for data filtering. By comparing the differences in number of decision between actual trajectories and the shortest path, we observed greater similarity in their distributions around the first peak. This implies that cyclists' route decision patterns align more closely with the shortest path when fewer decisions are made in a single trip.  However, around the second peak, differences emerged, with actual cycling trajectories exhibiting characteristics of high expectation, left-skewness, and long tails. In other words, within this range, cyclists' real route choices often deviate from the shortest path.
<p float="left">
  <img src="https://github.com/user-attachments/assets/b2bf4453-f704-4b3d-9ac8-3d062a9b0b71" width="80%" />
</p>
