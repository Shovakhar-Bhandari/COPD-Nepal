Chronic Obstructive Pulmonary Disease (COPD) is a significant health issue in Nepal, influenced by various factors and characterized by specific symptoms. Here’s a list of factors contributing to COPD and its common symptoms:

### Factors Contributing to COPD in Nepal

1. **Environmental Factors**:
   - **Air Pollution**: High levels of particulate matter from vehicles, industrial emissions, and biomass burning.
   - **Indoor Air Pollution**: Use of solid fuels (like wood and dung) for cooking and heating, leading to smoke exposure.
   - **Dust and Allergens**: Exposure to dust, mold, and pollen, especially in rural areas.

2. **Lifestyle Factors**:
   - **Smoking**: High prevalence of tobacco smoking and exposure to secondhand smoke.
   - **Occupational Exposures**: Jobs in agriculture, mining, and construction may expose individuals to harmful dust and chemicals.
   - **Sedentary Lifestyle**: Lack of physical activity can contribute to respiratory issues.

3. **Socioeconomic Factors**:
   - **Poverty**: Limited access to healthcare and education can exacerbate COPD management.
   - **Lack of Awareness**: Insufficient knowledge about COPD prevention and management.

4. **Health Factors**:
   - **Respiratory Infections**: History of recurrent respiratory infections, particularly in childhood.
   - **Genetic Factors**: Family history of respiratory diseases may increase susceptibility.
   - **Comorbidities**: Presence of other health issues such as asthma, diabetes, and cardiovascular diseases.

5. **Geographic Factors**:
   - **Topography**: High altitudes and varying climates may influence respiratory health.
   - **Urbanization**: Rapid urban growth contributing to increased pollution and lifestyle changes.

### Symptoms of COPD

1. **Chronic Cough**: A persistent cough that may produce mucus (sputum).
2. **Shortness of Breath**: Difficulty in breathing, especially during physical activities or exertion.
3. **Wheezing**: A whistling or squeaky sound while breathing, especially during exhalation.
4. **Chest Tightness**: A feeling of constriction or pressure in the chest.
5. **Increased Mucus Production**: Excessive phlegm that can lead to respiratory infections.
6. **Fatigue**: Persistent tiredness due to increased effort in breathing and reduced oxygen intake.
7. **Frequent Respiratory Infections**: Increased susceptibility to colds, flu, and other infections.
8. **Cyanosis**: A bluish tint to the lips or fingertips, indicating low oxygen levels.



# References for this study
- https://www.dovepress.com/factors-associated-with-chronic-obstructive-pulmonary-diseases-in-nepa-peer-reviewed-fulltext-article-COPD
- https://pubmed.ncbi.nlm.nih.gov/35615818/
- https://www.tandfonline.com/doi/full/10.2147/COPD.S268110
- https://www.who.int/home/search-results?indexCatalogue=genericsearchindex1&searchQuery=Chronic%20Obstructive%20Pulmonary%20Disease&wordsMode=AnyWord
- https://www.worldbank.org/en/search?q=Chronic+Obstructive+Pulmonary+Diseas
- https://www.tandfonline.com/doi/pdf/10.2147/COPD.S268110
- https://github.com/phenoflow/Chronic-Obstructive-Pulmonary-Disease---9387f040-1873-11ef-9de4-4d4ea830ad16?tab=readme-ov-file



### Key Findings : Insights from Visualizations of the COPD data
#### Introduction

Chronic Obstructive Pulmonary Disease (COPD) is a significant public health concern, particularly in regions like Nepal, where exposure to environmental pollutants, biomass fuels, and smoking remains prevalent. COPD is often underdiagnosed and undertreated, leading to high morbidity and mortality rates. To better understand the factors associated with COPD diagnosis in Nepal, we analyze a set of visualizations and a correlation matrix that highlights relationships between various environmental, lifestyle, and genetic factors with COPD diagnosis. This review critically evaluates these insights, incorporating data from box plots, violin plots, and correlation analysis.

#### Age and COPD Diagnosis

From the box plot visualization of age, it is evident that **age** does play a moderate role in the diagnosis of COPD. The median age of those diagnosed with COPD is slightly higher than that of those not diagnosed. For individuals diagnosed with COPD, the median age is around **60 years**, compared to **58 years** for non-COPD individuals. Although there is some overlap in the age distribution, the range extends from **45 to 75 years** for COPD patients, while non-COPD individuals range from **40 to 70 years**. This suggests that advancing age is a factor but not the most prominent one. The correlation matrix further supports this, showing a negative and weak correlation of **-0.027** between age and COPD diagnosis. Thus, while older individuals are somewhat more prone to COPD, age alone is not a significant predictor.

#### Smoking Status: A Dominant Risk Factor

Smoking status is, unsurprisingly, the most critical factor in determining COPD risk. The violin plot indicates that individuals who are current or former smokers have a much higher likelihood of being diagnosed with COPD. The shape of the violin plot is distinctly broader for current smokers with COPD, reflecting the higher density of diagnosed individuals. In contrast, the non-COPD group contains a greater proportion of never-smokers. 

The correlation matrix underscores this observation, with a **correlation coefficient of 0.62** between smoking status and COPD diagnosis, making smoking the strongest predictor. This correlation suggests that a higher proportion of individuals with a history of smoking—whether they currently smoke or have quit—are diagnosed with COPD. Current smokers show a strong association with COPD, aligning with the global understanding of the disease, where smoking is a leading cause of lung damage.

#### Environmental Factors: Biomass Fuel Exposure and Air Pollution

The dataset contains important environmental risk factors, such as **biomass fuel exposure** and **air pollution levels**. In Nepal, biomass fuel is commonly used for cooking and heating, especially in rural areas, which may contribute significantly to respiratory diseases like COPD.

The box plot of biomass fuel exposure shows a minimal difference between those diagnosed with COPD and those not diagnosed, suggesting an even distribution of exposure across both groups. However, the correlation matrix reveals a moderate positive correlation between biomass fuel exposure and COPD diagnosis, with a **correlation coefficient of 0.28**. This indicates that exposure to biomass fuels contributes to COPD but is not as influential as smoking.

**Air pollution levels**, another significant environmental factor, show a similar pattern. The box plot highlights that individuals diagnosed with COPD are exposed to slightly higher levels of air pollution than those without COPD. However, there are outliers in the non-COPD group, suggesting that some individuals without COPD are also exposed to high pollution levels. The correlation between air pollution and COPD diagnosis is **0.089**, which, while positive, is relatively weak. This suggests that although air pollution is a contributing factor, it does not have as direct or strong an impact on COPD diagnosis in this dataset compared to other variables like smoking or family history.

#### Genetic Predisposition: Family History of COPD

The role of genetics in COPD development is evident through the inclusion of **family history of COPD** in the dataset. The correlation between family history and COPD diagnosis is **0.31**, indicating a moderate positive relationship. This implies that individuals with a family history of the disease are more likely to be diagnosed with COPD, potentially due to both genetic factors and shared environmental exposures such as smoking or biomass fuel use.

While family history is not as strong a predictor as smoking, it is still an important factor. The moderate correlation value suggests that genetic predisposition, combined with environmental triggers, plays a significant role in the development of COPD.

#### Occupational Exposure and COPD Diagnosis

The dataset includes **occupational exposure**, which is often linked to respiratory diseases in many countries, particularly for individuals working in environments with dust, chemicals, or other harmful substances. Interestingly, the box plot for occupational exposure shows only a slight difference between the COPD and non-COPD groups, and the correlation matrix reveals a weak correlation of **0.043** with COPD diagnosis. This suggests that, in this specific dataset, occupational exposure may not be a key factor, possibly due to the nature of occupations represented or other variables taking precedence.

#### Other Factors: Gender, BMI, and Childhood Infections

Several other factors were also analyzed, including **gender**, **BMI**, and **respiratory infections in childhood**. These variables show minimal influence on COPD diagnosis:
- **Gender** has a weak negative correlation of **-0.03**, indicating that men and women are almost equally likely to be diagnosed with COPD in this dataset.
- **BMI** has an even weaker negative correlation of **-0.0085**, suggesting that body weight does not have a significant impact on the likelihood of COPD diagnosis.
- **Respiratory infections in childhood** show a negligible correlation of **0.017** with COPD, meaning that while childhood infections can damage the lungs and potentially predispose individuals to respiratory issues, their impact on COPD development in adulthood is minor in this dataset.

#### Conclusion

The analysis of the COPD dataset for Nepal reveals several key insights. **Smoking status** is the most significant factor associated with COPD diagnosis, as demonstrated by both the violin plot and a strong positive correlation of **0.62**. Other factors, such as **biomass fuel exposure** and **family history**, also play moderate roles, with correlation coefficients of **0.28** and **0.31**, respectively. In contrast, **age**, **air pollution**, **occupational exposure**, and other variables exhibit weaker correlations, suggesting they are contributing factors but not as central in this particular dataset.

This analysis highlights the multifactorial nature of COPD, where both lifestyle choices (such as smoking) and environmental exposures (biomass fuel and air pollution) interact with genetic predispositions to influence the development of the disease. Moving forward, public health interventions in Nepal should focus on reducing smoking rates and limiting exposure to harmful environmental factors like biomass fuels, while further research into genetic risk factors may offer additional insights into COPD prevention and treatment.


