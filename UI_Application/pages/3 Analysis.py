# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Heart Disease Dashboard",
                   page_icon=":heart:", layout="wide")

# Load the heart disease dataset
df = pd.read_csv('./dataset/cleaned_dataset_heart.csv')

# Function for displaying the dashboard


def show_dashboard():
    # st.write("---")
    st.subheader('Heart Disease Dataset Dashboard')
    col1, col2 = st.columns(2)

    with col1:
        st.image("./images/Dataset_desp.png")

    with col2:
        st.write(df)

    # Visualize the relationships between variables
    st.subheader('Visualization of Variables')

    # Create the columns
    col1, col2, col3 = st.columns(3)

    # Display plots in the first row
    with col1:
        # Age distribution
        st.write('Age Distribution')
        fig, ax = plt.subplots(figsize=(8, 6))  # Create figure and axes
        sns.histplot(df['age'], ax=ax)  # Use the created axes for plotting
        st.pyplot(fig)

    with col2:
        # Gender distribution
        st.write('Gender Distribution')
        gender_counts = df['sex'].value_counts()

        # Create bar chart
        fig, ax = plt.subplots()
        ax.bar(gender_counts.index, gender_counts.values)

        # Set labels and title
        ax.set_ylabel('Counts')
        ax.set_title('Gender Distribution')

        # Set custom x-axis labels
        # Setting custom labels for the ticks
        plt.xticks([0, 1], ['0: Female', '1: Male'])

        # Set x-axis label
        ax.set_xlabel('Gender')

        # Show plot in Streamlit
        st.pyplot(fig)

    with col3:
        # Resting Blood Pressure distribution
        st.write('Resting Blood Pressure Distribution')
        fig, ax = plt.subplots(figsize=(8, 6))  # Create figure and axes
        # Use the created axes for plotting
        sns.histplot(df['resting_bp_s'], ax=ax)
        st.pyplot(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Cholesterol distribution
        st.write('Cholesterol Distribution')
        fig, ax = plt.subplots(figsize=(8, 6))  # Create figure and axes
        # Use the created axes for plotting
        sns.histplot(df['cholesterol'], ax=ax)
        st.pyplot(fig)

    with col2:
        st.write('Fasting Blood Sugar Distribution')
        fasting_blood_sugar_counts = df['fasting_blood_sugar'].value_counts()

        # Create bar chart
        fig, ax = plt.subplots()
        ax.bar(fasting_blood_sugar_counts.index,
               fasting_blood_sugar_counts.values)

        # Set labels and title
        ax.set_ylabel('Counts')
        ax.set_title('Fasting Blood Sugar Distribution')

        # Set custom x-axis labels
        # Setting custom labels for the ticks
        plt.xticks([0, 1], ['0: <120 mg/dL', '1: >120 mg/dL'])

        # Set x-axis label
        ax.set_xlabel('Fasting Blood Sugar')

        # Show plot in Streamlit
        st.pyplot(fig)

    with col3:
        # Visualization for resting ECG
        st.write('Resting ECG Distribution')
        resting_ecg_counts = df['resting_ecg'].value_counts()
        st.bar_chart(resting_ecg_counts)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Visualization for maximum heart rate (already updated)
        st.write('Maximum Heart Rate Distribution')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(df['max_heart_rate'], kde=True, ax=ax)
        st.pyplot(fig)

    with col2:
        # Visualization for exercise-induced angina (check for consistent approach)
        st.write('Exercise-Induced Angina Distribution')
        exercise_angina_counts = df['exercise_angina'].value_counts()
        st.bar_chart(exercise_angina_counts)

    with col3:
        # Visualization for oldpeak (updated)
        st.write('Oldpeak Distribution')
        fig, ax = plt.subplots(figsize=(8, 6))
        # Consider removing `kde=True` if not needed
        sns.histplot(df['oldpeak'], kde=True, ax=ax)
        st.pyplot(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Visualization for ST slope
        st.write('ST Slope Distribution')
        st_slope_counts = df['ST_slope'].value_counts()
        st.bar_chart(st_slope_counts)

    with col2:
        # Visualization for target variable
        st.write('Target Variable Distribution')
        target_counts = df['target'].value_counts()
        st.bar_chart(target_counts)

    # Visualization for non-target variables vs target variable
    # st.header('Non-Target Variables vs Target Variable')
    # non_target_columns = [col for col in df.columns if col not in ['target']]
    # for col in non_target_columns:
    #     st.subheader(f'{col} vs Target')
    #     fig, ax = plt.subplots(figsize=(8, 6))  # Create figure and axes
    #     sns.countplot(x=col, hue='target', data=df, ax=ax)  # Use the created axes for plotting
    #     st.pyplot(fig)  # Pass the figure object to st.pyplot()

    # Continuous vs. Continuous
    st.write('**Continuous vs. Continuous**')

    col1, col2, col3 = st.columns(3)

    with col1:
        # Age vs. Max Heart Rate
        st.write('Age vs. Max Heart Rate')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x='age', y='max_heart_rate', data=df, ax=ax)
        st.pyplot(fig)

    with col2:
        # Resting Blood Pressure vs. Cholesterol
        st.write('Resting Blood Pressure vs. Cholesterol')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x='resting_bp_s', y='cholesterol', data=df, ax=ax)
        st.pyplot(fig)

    with col3:
        # Oldpeak vs. Max Heart Rate
        st.write('Oldpeak vs. Max Heart Rate')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x='oldpeak', y='max_heart_rate', data=df, ax=ax)
        st.pyplot(fig)

    # Continuous vs. Categorical
    st.write('**Continuous vs. Categorical**')

    col1, col2, col3 = st.columns(3)

    with col1:
                
        st.write('Age Distribution by Target Variable')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(x='age', hue='target', data=df, bins='auto', ax=ax) 
        st.pyplot(fig)

    with col2:
        # Sex vs. Target Variable
        st.write('Sex vs. Target Variable')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x='sex', hue='target', data=df, ax=ax)
        st.pyplot(fig)

    with col3:
        # Fasting Blood Sugar vs. Target Variable
        st.write('Fasting Blood Sugar vs. Target Variable')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x='fasting_blood_sugar', hue='target', data=df, ax=ax)
        st.pyplot(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Resting ECG vs. Target Variable (consider bar chart or boxplot)
        st.write('Resting ECG vs. Target Variable')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x='resting_ecg', hue='target', data=df,
                    ax=ax)  # Adjust based on data
        st.pyplot(fig)

    with col2:
        # Exercise Angina vs. Target Variable
        st.write('Exercise Angina vs. Target Variable')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x='exercise_angina', hue='target', data=df, ax=ax)
        st.pyplot(fig)

    with col3:
        # ST Slope vs. Target Variable
        st.write('ST Slope vs. Target Variable')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x='ST_slope', hue='target', data=df, ax=ax)
        st.pyplot(fig)

    # Categorical vs. Categorical
    st.write('**Categorical vs. Categorical**')

    col1, col2 = st.columns(2)

    with col1:
        # Chest Pain Type vs. Target Variable
        st.write('Chest Pain Type vs. Target Variable')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x='chest_pain_type', hue='target', data=df, ax=ax)
        st.pyplot(fig)

    with col2:
        # Exercise Angina vs. Chest Pain Type
        st.write('Exercise Angina vs. Chest Pain Type')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x='chest_pain_type',
                      hue='exercise_angina', data=df, ax=ax)
        st.pyplot(fig)

    # Show correlation mgraphs of all variables
    st.subheader('Relation b/w all variables')
    # Create the pairplot using Seaborn
    fig = sns.pairplot(df)
    # Display the pairplot on the Streamlit dashboard
    st.pyplot(fig)

    # Show correlation heatmap
    st.subheader('Correlation Heatmap')
    fig, ax = plt.subplots(figsize=(10, 8))  # Create figure and axes
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f',
                ax=ax)  # Use the created axes for plotting
    st.pyplot(fig)  # Pass the figure object to st.pyplot()


# Create a button for displaying the dashboard
show_dashboard()
