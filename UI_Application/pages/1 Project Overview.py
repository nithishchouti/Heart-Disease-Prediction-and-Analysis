import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='CVD Prediction | Project Overview',
    page_icon=":heart:"
)

st.title("Data Analysis and Visualization for Cardiovascular Disease Prediction")

st.header("Project Overview")

with st.container():
    st.subheader("Project Scope:")
    st.write("""
            - The project focuses on predicting cardiovascular diseases (CVDs) by analyzing historical patient data, developing predictive models, and enhancing healthcare outcomes through data-driven insights.
            - Predicting CVDs is crucial for early intervention and prevention, reducing mortality rates, and improving patient outcomes and quality of life.
            - Data analysis and visualization play a vital role in uncovering patterns, trends, and insights from complex healthcare data, aiding in decision-making and improving patient care.
            - Historical patient data is analyzed to identify risk factors associated with CVDs, enabling the development of effective predictive models.
            - Predictive models are created based on identified risk factors to forecast the likelihood of CVD occurrence in individuals.
            """)

    st.write("""
            <div style="margin: 50px;">      
            </div>
            """, unsafe_allow_html=True)

with st.container():
    st.subheader("Dataset Description:")

    st.markdown("#### Heart-Disease-Dataset-(Comprehensive)")
    st.write("Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year which is about 32 of all deaths globally. CVDs are a group of disorders of the heart and blood vessels and include coronary heart disease, cerebrovascular disease, rheumatic heart disease, and other conditions. Four out of 5CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. The five datasets used for the curation of the comprehensive dataset with 11 features in common are database of instances:")
    with st.container():
        st.write("""
                - Cleveland: 303
                - Hungarian: 294
                - Switzerland: 123
                - Long Beach VA: 200
                - Stalog (Heart) Data Set: 270
                """)

    st.write(
        "For Dataset Link:- [Click Here](https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive)")

    st.write("Number of instances: 1190")
    st.write("Number of features: 12")

    st.info("""Source: 
            - https://ieee-dataport.org/
            - https://openml.org/""")
    st.write("""
            <div style="margin: 50px;">
             
            </div>
            """, unsafe_allow_html=True)

with st.container():
    st.subheader("Dataset Features:")
    st.markdown("#### Heart Disease Dataset Attribute Description")
    data = {'S.No.': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'Attribute': ['age', 'sex', 'chest pain type', 'resting blood pressure', 'serum cholesterol', 'fasting blood sugar', 'resting electrocardiogram results', 'maximum heart rate achieved', 'exercise induced angina', 'oldpeak =ST', 'the slope of the peak exercise ST segment', 'class'],
            'Code given': ['age', 'sex', 'chest_pain_type', 'resting_bp_s', 'cholesterol', 'fasting_blood_sugar', 'resting_ecg', 'max_heart_rate', 'exercise_angina', 'oldpeak', 'ST_slope', 'target'],
            'Unit': ['in years', '1, 0 ', '1,2,3,4', 'in mm Hg', 'in mg/dl', ' 1,0 > 120 mg/dl', '0,1,2', '60–202', '0,1', '0.0 - 6.2', '0,1,2', '0,1'],
            'Data type': ['Numeric', 'Binary', 'Nominal', 'Numeric', 'Numeric', 'Binary', 'Nominal', 'Numeric', 'Binary', 'Numeric', 'Nominal', 'Binary']}
    df = pd.DataFrame(data)
    st.write(df, width=800)
    st.write("""
            <div style="margin: 20px;">
             
            </div>
            """, unsafe_allow_html=True)

    st.markdown("#### Description of Attributes")
    st.markdown("**- Sex (Binary):** 1 = Male, 0 = Female")
    st.markdown("**- Chest Pain type (Nominal):** Angina is a type of chest pain that occurs when the heart muscle doesn't receive enough oxygen-rich blood. It's often described as a squeezing, pressure, or discomfort in the chest, typically triggered by physical exertion or emotional stress.")
    st.write("""
            - Value 1: typical angina
            - Value 2: atypical angina
            - Value 3: non-anginal pain
            - Value 4: asymptomatic
            """)
    st.markdown("**- Resting blood pressure (Numeric):** a key feature in heart disease prediction models, serves as an indicator of cardiovascular health, reflecting the pressure exerted on artery walls between heartbeats.")
    st.write("""
            - Measured in mm Hg.
            """)
    st.markdown("**- Serum Cholesterol (Numeric):** an integral component in heart disease prediction models, signify the concentration of cholesterol in the bloodstream, highlighting its association with arterial plaque formation and cardiovascular risk.")
    st.write("""
            - Measured in mg/dl.
            """)
    st.markdown("**- Fasting Blood Sugar (Binary):** pivotal in heart disease prediction models, signify the concentration of glucose in the bloodstream after a period of fasting, serving as a crucial marker for assessing metabolic health and diabetes risk, which are significant factors in cardiovascular disease development.")
    st.write("""
            - 1 if faster blood sugar > 120 mg/dl
            - 0 if faster blood sugar <= 120 mg/dl 
            """)
    st.markdown("**- Resting Electrocardiogram Results(Nominal):** Resting ECG results, a cornerstone of heart disease prediction models, provide insights into the electrical activity of the heart at rest, aiding in the detection of abnormalities such as arrhythmias, ischemia, and structural heart diseases, crucial for assessing cardiovascular health and risk.")
    st.write("""
            - Value 0: normal
            - Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
            - Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
            """)
    st.markdown("**- Maximum Heart Read(Numeric):** a vital parameter in heart disease prediction models, represents the highest number of heartbeats per minute achievable during intense physical activity. It serves as a crucial metric for evaluating cardiovascular fitness and assessing individual exercise tolerance, aiding in risk stratification and prognosis determination for heart-related conditions.")
    st.write("""
            - Value Range: 60-202
            """)
    st.markdown("**- Exercise Induced Angina(Binary):** manifests as chest pain or discomfort provoked by physical exertion, indicating inadequate blood flow to the heart during increased activity, pivotal in diagnosing and managing coronary artery disease.")
    st.write("""
            - 1 = yes
            - 0 = no 
            """)
    st.markdown("**- Oldpeak(Numeric):** measured during exercise testing, represents the extent of ST segment depression compared to rest, indicating the degree of myocardial ischemia and providing valuable prognostic information in assessing cardiovascular risk.")
    st.write("""
            - Value Range: 0.0 - 6.2            
            """)
    st.markdown("**- ST slope (Nominal):** observed in an electrocardiogram during exercise testing, signifies the direction and magnitude of ST segment deviation relative to the baseline, serving as a crucial indicator of myocardial ischemia severity and aiding in risk stratification for cardiovascular events.")
    st.write("""
            - Value 1: Unsloping
            - Value 2: Flat
            - Value 3: Downsloping
            """)
    st.markdown(
        "**- Class/Target (Binary):** Predicts whether a person is actually suffering from Heart disease.")
    st.write("""
            - 1 = Heart disease
            - 0 = Normal
            """)
    st.write("""
            <div style="margin: 50px;">
             
            </div>
            """, unsafe_allow_html=True)

with st.container():
    st.subheader("Machine Learning algorithms used:")
    st.write("""
             - Logistic Regression (Scikit-learn)
             - Naive Bayes (Scikit-learn)
             - Support Vector Machine (Linear) (Scikit-learn)
             - K-Nearest Neighbours (Scikit-learn)
             - Decision Tree (Scikit-learn)
             - Random Forest (Scikit-learn)
             - XGBoost (Scikit-learn)
             - Artificial Neural Network with 3 Hidden layer (Keras)
            """)

    st.write("""
            <div style="margin: 50px;">
             
            </div>
            """, unsafe_allow_html=True)

with st.container():
    st.subheader("Evaluation Metrics:")
    st.markdown(
        "**Accuracy Score**")
    st.write("""
             - The evaluation metric used in the code snippet is Accuracy, which measures the proportion of correctly classified instances out of the total instances.
             - The accuracy scores for different machine learning algorithms are calculated and displayed using a bar plot, with the algorithm having the highest accuracy score considered to perform better in terms of overall prediction accuracy.
            """)

    st.write("""
            <div style="margin: 50px;">
             
            </div>
            """, unsafe_allow_html=True)

with st.container():
    st.subheader("Conclusion:")
    st.markdown(
        "After executing various models with the defined features and preprocessing, we come to the conclusion that Random Forest Classifier provides the best results for the prediction of Cardiovascular disease with an accuracy score of 89.5 % for the given dataset.")
    st.markdown(
        "Camparison of various algorithms with respect to their Accuracy Scores:-")
    st.write("""
             - The accuracy score achieved using Logistic Regression is: 83.43 %
             - The accuracy score achieved using Random Forest is: 89.5 %
             - The accuracy score achieved using Support Vector Machine is: 71.27 %
             - The accuracy score achieved using K-Nearest Neighbors is: 69.61 %
             - The accuracy score achieved using Decision Tree is: 80.11 %
             - The accuracy score achieved using Naive Bayes is: 85.08 %
             - The accuracy score achieved using XGBoost is: 87.85 %
             - The accuracy score achieved using Neural Network is: 82.87 %
            """)

    st.image("images/accuracy.png")
    st.write("""
            <div style="margin: 50px;">
             
            </div>
            """, unsafe_allow_html=True)


with st.container():
    st.subheader("Reference Paper used:")
    st.write("""
             - Name: Predictive Modeling for Heart Disease Detection with Machine Learning.
                - Link: [https://ieeexplore.ieee.org/abstract/document/10402340]
             - Name: Automated Heart Disease Prediction System using Machine Learning Approaches.
                - Link: [https://ieeexplore.ieee.org/abstract/document/10407008]
             - Name: AI Models for Early Detection and Mortality Prediction in Cardiovascular Diseases.
                - Link: [https://www.techrxiv.org/doi/full/10.36227/techrxiv.24248827.v1]
             - Name: A Study on Heart Disease Prediction using Different Classification Models based on Cross Validation Method.
                - Link: [https://www.ijert.org/a-study-on-heart-disease-prediction-using-different-classification-models-based-on-cross-validation-method]    
             """)


with st.container():
    st.subheader("Team Members:")
    left, middle, right = st.columns(3)
    with left:
        # st.image("images/nithish.jpeg")
        st.write("Nithish Chouti")
    with middle:
        # st.image("images/udayini.jpeg")
        st.write("Udayini Vedantham")
    with right:
        # st.image("images/karan.jpg")
        st.write("Karan R Naik")
