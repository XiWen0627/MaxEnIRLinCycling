# MaxEnDeepIRL Application for uncovering visual preference in cycling route decision procedure.
XiWen0627's Master Project : Unraveling  Built Environment Preference to Route Choice via IRL Approach 

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

First of all, we identified and eliminated the counter-intuitive cycling trips in order to enhance data quility. Specifically, we filtered out trips less than 3 minutes or exceeding one hour, considering the rebalancing process. Additionally, we removed the trajectory points where speeds exceeded 30 km/h, likely due to poor GPS signal. Following this data cleaning process, we obtained a dataset of **10,000** distinct cycling trips suitable for map matching.

Second, we mapped trajectory points onto the road network using a Hidden Markov Model(HMM) to better approximate the link-based decision-making process of DBS cycling. This method successfully assigned a sequence of road segments to the trajectory points. Furthermore, to validate the effectiveness of map-matching process, we randomly selected several mapped trajectories and compared them with raw data. As shown in **Figure 1**, this comparison demonstrated convincing result.

Finally, we filtered the mapped DBS trajectory data using specific criteria informed by preliminary literature reviews and exploratory analysis. Given the subtropical location and an average November temperature of 19.7℃, our data comprehensively represented cycling behavior. To account for the direct impact of weather conditions on cycling, we excluded data from two rainy days(Nov 9th and Nov 16th). Additionally, to mitigate potential biases in estimating preferences due to temporal changes, we focused our analysis on cyclists' behaviors during weekdays and daylight hours. Furthermore, our DBS trajectories deviated significantly from the shortest path when applying the Dijkstra Algorithm, aligning with findings in current literature. Specifically, approximately 83.8% of cyclists selected the shortest path for trips involving fewer than five road segments. Therefore, we concentrated on cycling trips with more than 5 road segments, resulting in **10000** distinct trip trajectories as the valid dataset for further investigation. The results of exploratory data analysis are shown in Appendix 1.

#### Street View Images


## Methodology
## Appendix 1. Exploratory Data Analysis for DBS Trajectory Data
