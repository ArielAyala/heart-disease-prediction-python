import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Configure the Streamlit page (Set up page title, layout, and sidebar state)
st.set_page_config(page_title='Heart disease prediction',
                   layout='centered',
                   initial_sidebar_state='auto')

# Title of the app
st.title('App to predict heart disease')
st.markdown("""___""")  # Divider line for better presentation

# Display a logo in the sidebar (Optional)
logo = 'logo.jpeg'
st.sidebar.image(logo, width=150)

# Sidebar section for user data input
st.sidebar.header('Data entered by the user')

# Option to upload a CSV file (The user can upload a CSV file with input data)
uploaded_file = st.sidebar.file_uploader('Upload the CSV file', type=['csv'])

# Check if the user has uploaded a CSV file
if uploaded_file is not None:
    # Load the CSV file into a pandas DataFrame
    input_df = pd.read_csv(uploaded_file)
else:
    # Function to create sliders and input fields for user to manually enter data
    def user_input_features():
        sbp = st.sidebar.slider('Systolic blood pressure', 101, 218, 150)  # Systolic blood pressure slider
        tabacco = st.sidebar.slider('Accumulated tobacco (kg)', 0.00, 31.20, 2.00)  # Tobacco consumption slider
        ldl = st.sidebar.slider('Low-density lipoprotein cholesterol', 0.98, 15.33, 4.34)  # LDL cholesterol slider
        adiposity = st.sidebar.slider('Adiposity', 6.64, 42.49, 26.12)  # Adiposity (body fat) slider
        family = st.sidebar.selectbox('Family history of heart disease', ('Present', 'Absent'))  # Family history dropdown
        type = st.sidebar.slider('Type', 13, 78, 53)  # Type (numeric field, potentially a custom feature)
        obesity = st.sidebar.slider('Obesity', 14.70, 46.58, 25.80)  # Obesity level slider
        alcohol = st.sidebar.slider('Current alcohol consumption', 0.00, 147.19, 7.51)  # Alcohol consumption slider
        age = st.sidebar.slider('Age', 15, 64, 45)  # Age slider

        # Store all the inputs into a dictionary
        data = {'sbp': sbp,
                'Tobacco': tabacco,
                'ldl': ldl,
                'Adiposity': adiposity,
                'Family': family,
                'Type': type,
                'Obesity': obesity,
                'Alcohol': alcohol,
                'Age': age
                }
        # Convert the dictionary into a pandas DataFrame for model input
        features = pd.DataFrame(data, index=[0])
        return features
    
    # Call the function to get user input or default values in the DataFrame
    input_df = user_input_features()

# Apply LabelEncoder to convert the 'Family' column (categorical) into numerical values
encoder = LabelEncoder()
input_df['Family'] = encoder.fit_transform(input_df['Family'])

# Select only the first row of the input DataFrame (This might be to ensure a single prediction)
input_df = input_df[:1]

# Display the user-entered data in the app
st.subheader('Data entered by the user')

# If a CSV is uploaded, display its content; otherwise, show the manually entered data
if uploaded_file is not None:
    st.write(input_df)  # Display the uploaded CSV data
else:
    st.write('Waiting for CSV file to load, currently using example input parameters (shown below)')
    st.write(input_df)  # Display default data input

# Load the pre-trained classification model from a .pkl file
load_clf = pickle.load(open('heart.pkl', 'rb'))

# Make a prediction based on the input data using the loaded model
prediction = load_clf.predict(input_df)

# Get the probability of the prediction (useful for displaying confidence level)
prediction_probability = load_clf.predict_proba(input_df)

# Divide the app layout into two columns to display the prediction and its probability side by side
col1, col2 = st.columns(2)

# Display the prediction result (heart disease or no heart disease)
with col1:
    st.subheader('Prediction')
    st.write(prediction)
    
# Display the prediction probability (confidence score of the model)
with col2: 
    st.subheader('Probability of prediction')
    st.write(prediction_probability)
    
# Output whether the person has heart disease based on the prediction result
if prediction == 0:
    st.subheader('The person has no heart problems')
else:
    st.subheader('The person has heart problems')

# Divider line for cleaner UI
st.markdown("""___""")
