import streamlit as st

st.set_page_config(
    page_title='CVD Prediction',
    page_icon=":heart:",
)

st.title("Heart Health Insights: Analysing Data and Visualising Predictive Factors for Cardiovascular Disease")

st.header("Introduction")
with st.container():
    st.subheader("Understanding Cardiovascular Disease:")
    left_column, right_column = st.columns(2)

    with left_column:
        st.write("Cardiovascular disease (CVD) refers to a group of conditions affecting the heart and blood vessels, including coronary artery disease, heart failure, and stroke. It is the leading cause of death globally, with risk factors such as high blood pressure, cholesterol, smoking, and obesity contributing significantly to its development. Understanding CVD involves recognizing its multifaceted nature and the importance of preventive measures and early detection in reducing its impact.")

    with right_column:
        st.image("images/94525669.jpg")

st.header("Insights into Cardiovascular Disease")
with st.container():
    st.subheader("Causes and Risk Factors:")
    st.write("Cardiovascular disease (CVD) arises from a complex interplay of genetic, environmental, and lifestyle factors. Common causes and risk factors include hypertension, high cholesterol levels, smoking, diabetes, obesity, sedentary lifestyle, and unhealthy dietary habits. Understanding and addressing these modifiable risk factors are crucial in preventing the onset and progression of CVD.")
    st.image("images/Risk-factors-of-cardiovascular-disease.png")

with st.container():
    st.subheader("Prevention:")
    st.write("Preventing cardiovascular disease involves adopting a heart-healthy lifestyle, including regular physical activity, maintaining a balanced diet rich in fruits, vegetables, and whole grains, avoiding smoking and excessive alcohol consumption, managing stress levels, and monitoring blood pressure and cholesterol levels regularly. Early detection and management of risk factors play a pivotal role in reducing the burden of cardiovascular disease.")

st.header("Statistics and Facts")
with st.container():
    st.image("images/Heart-Disease-CVD-Cardiovascular-Disease.jpg")
    st.write("""
    - Cardiovascular disease (CVD) is the leading cause of death globally, accounting for approximately 17.9 million deaths annually.
    - According to the World Health Organization (WHO), an estimated 31% of all global deaths are attributed to cardiovascular diseases.
    - Heart attacks and strokes are the most common manifestations of CVD, with nearly 85% of cardiovascular deaths occurring due to heart attacks and strokes.
    - High blood pressure, a major risk factor for CVD, affects approximately 1.13 billion people worldwide.
    - Despite advances in medical treatment, CVD remains a significant public health challenge, particularly in low- and middle-income countries where access to healthcare services and preventive measures may be limited.
    """)
