import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title='CVD Prediction | Prediction',
    page_icon=":heart:"
)


def load_model():
    model_filename = 'model.pkl'
    with open(model_filename, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model


def main():
    model = load_model()

    st.title("Data Analysis and Visualization for Cardiovascular Disease Prediction")
    st.header("Prediction:")

    # Get user input
    age = st.number_input("Age", 0, 100)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    sex_num = 1 if sex == 'Male' else 0
    cp = st.selectbox('Chest Pain Type', [
                      'Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    cp_num = cp.index(cp)
    resting_bp = st.slider('Resting Blood Pressure (in mm Hg)', 90, 200, 120)
    chol = st.slider('Cholesterol (in mg/dl)', 100, 600, 250)
    fbs = st.selectbox('Fasting Blood Sugar (> 120 mg/dl)', ['False', 'True'])
    fbs_num = fbs.index(fbs)
    restecg = st.selectbox('Resting Electrocardiographic Results', [
                           'Normal', 'ST-T Abnormality', 'Left Ventricular Hypertrophy'])
    restecg_num = restecg.index(restecg)
    max_HR = st.slider('Maximum Heart Rate Achieved (71-202)', 70, 220, 150)
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
    exang_num = exang.index(exang)
    oldpeak = st.slider(
        'ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 1.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [
                         'Upsloping', 'Flat', 'Downsloping'])
    slope_num = slope.index(slope)

    if st.button('Predict'):
        user_input = pd.DataFrame(data={
            'age': [age],
            'sex': [sex_num],
            'chest_pain_type': [cp_num],
            'resting_bp_s': [resting_bp],
            'cholesterol': [chol],
            'fasting_blood_sugar': [fbs_num],
            'resting_ecg': [restecg_num],
            'max_heart_rate': [max_HR],
            'exercise_angina': [exang_num],
            'oldpeak': [oldpeak],
            'ST_slope': [slope_num],
        })

        prediction = model.predict(user_input)
        # prediction_proba = model.predict_proba(user_input)

        if prediction[0] == 1:
            bg_color = 'green'
            prediction_result = 'Negative'
            st.markdown(
                f"<p style='background-color:{bg_color}; color:white; padding:10px;'>Prediction: {prediction_result}<br>The model predicts that there is less possibility of Cardiovascular Disease!</p>", unsafe_allow_html=True)

        else:
            bg_color = 'red'
            prediction_result = 'Positive'
            st.markdown(
                f"<p style='background-color:{bg_color}; color:white; padding:10px;'>Prediction: {prediction_result}<br>The model predicts a possibility of Cardiovascular Disease!</p>", unsafe_allow_html=True)


_ = """
        if prediction[0] == 1:
            bg_color = 'green'
            prediction_result = 'Negative'
        else:
            bg_color = 'red'
            prediction_result = 'Positive'

        confidence = prediction_proba[0][1] if prediction[0] == 1 else prediction_proba[0][0]
        st.markdown(
            f"<p style='background-color:{bg_color}; color:white; padding:10px;'>Prediction: {prediction_result}<br>Confidence: {((confidence*10000)//1)/100}%</p>", unsafe_allow_html=True)
"""

if __name__ == '__main__':
    main()
