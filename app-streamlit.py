import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Configure the Streamlit page (Set up page title, layout, and sidebar state)
st.set_page_config(page_title='Heart disease prediction',
                   layout='centered',
                   initial_sidebar_state='auto')

# Language selector in the sidebar
language = st.sidebar.selectbox("Select Language / Seleccione el Idioma", ("English", "Español"))

# Define text content for both languages
if language == "English":
    title = 'App to predict heart disease'
    sidebar_header = 'Data entered by the user'
    upload_label = 'Upload the CSV file'
    sbp_label = 'Systolic blood pressure'
    tobacco_label = 'Accumulated tobacco (kg)'
    ldl_label = 'Low-density lipoprotein cholesterol'
    adiposity_label = 'Adiposity'
    family_label = 'Family history of heart disease'
    family_options = ('Present', 'Absent')
    type_label = 'Type'
    obesity_label = 'Obesity'
    alcohol_label = 'Current alcohol consumption'
    age_label = 'Age'
    subheader_input = 'Data entered by the user'
    waiting_text = 'Waiting for CSV file to load, currently using example input parameters (shown below)'
    prediction_label = 'Prediction'
    probability_label = 'Probability of prediction'
    no_heart_problems_text = 'The person has no heart problems'
    heart_problems_text = 'The person has heart problems'
else:
    title = 'Aplicación para predecir enfermedades del corazón'
    sidebar_header = 'Datos ingresados por el usuario'
    upload_label = 'Sube el archivo CSV'
    sbp_label = 'Presión arterial sistólica'
    tobacco_label = 'Tabaco acumulado (kg)'
    ldl_label = 'Colesterol de lipoproteínas de baja densidad (LDL)'
    adiposity_label = 'Adiposidad'
    family_label = 'Historial familiar de enfermedades cardíacas'
    family_options = ('Presente', 'Ausente')
    type_label = 'Tipo'
    obesity_label = 'Obesidad'
    alcohol_label = 'Consumo actual de alcohol'
    age_label = 'Edad'
    subheader_input = 'Datos ingresados por el usuario'
    waiting_text = 'Esperando la carga del archivo CSV, usando parámetros de entrada de ejemplo (mostrados a continuación)'
    prediction_label = 'Predicción'
    probability_label = 'Probabilidad de la predicción'
    no_heart_problems_text = 'La persona no tiene problemas cardíacos'
    heart_problems_text = 'La persona tiene problemas cardíacos'

# Title of the app
st.title(title)
st.markdown("""___""")  # Divider line for better presentation

# Display a logo in the sidebar (Optional)
logo = 'logo.jpeg'
st.sidebar.image(logo, width=150)

# Sidebar section for user data input
st.sidebar.header(sidebar_header)

# Option to upload a CSV file (The user can upload a CSV file with input data)
uploaded_file = st.sidebar.file_uploader(upload_label, type=['csv'])

# Check if the user has uploaded a CSV file
if uploaded_file is not None:
    # Load the CSV file into a pandas DataFrame
    input_df = pd.read_csv(uploaded_file)
else:
    # Function to create sliders and input fields for user to manually enter data
    def user_input_features():
        sbp = st.sidebar.slider(sbp_label, 101, 218, 150)  # Systolic blood pressure slider
        tabacco = st.sidebar.slider(tobacco_label, 0.00, 31.20, 2.00)  # Tobacco consumption slider
        ldl = st.sidebar.slider(ldl_label, 0.98, 15.33, 4.34)  # LDL cholesterol slider
        adiposity = st.sidebar.slider(adiposity_label, 6.64, 42.49, 26.12)  # Adiposity (body fat) slider
        family = st.sidebar.selectbox(family_label, family_options)  # Family history dropdown
        type = st.sidebar.slider(type_label, 13, 78, 53)  # Type (numeric field, potentially a custom feature)
        obesity = st.sidebar.slider(obesity_label, 14.70, 46.58, 25.80)  # Obesity level slider
        alcohol = st.sidebar.slider(alcohol_label, 0.00, 147.19, 7.51)  # Alcohol consumption slider
        age = st.sidebar.slider(age_label, 15, 64, 45)  # Age slider

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
st.subheader(subheader_input)

# If a CSV is uploaded, display its content; otherwise, show the manually entered data
if uploaded_file is not None:
    st.write(input_df)  # Display the uploaded CSV data
else:
    st.write(waiting_text)
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
    st.subheader(prediction_label)
    st.write(prediction)
    
# Display the prediction probability (confidence score of the model)
with col2: 
    st.subheader(probability_label)
    st.write(prediction_probability)
    
# Output whether the person has heart disease based on the prediction result
if prediction == 0:
    st.subheader(no_heart_problems_text)
else:
    st.subheader(heart_problems_text)

# Divider line for cleaner UI
st.markdown("""___""")
