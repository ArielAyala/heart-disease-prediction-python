import streamlit as st
import pandas as pd
from prediction import load_model, preprocess_input, make_prediction

# Configure Streamlit page
st.set_page_config(page_title='Heart disease prediction', layout='centered', initial_sidebar_state='auto')

# Language selector in the sidebar
language = st.sidebar.selectbox("Select Language / Seleccione el Idioma", ("English", "Español"))

# Define texts based on the selected language
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
st.markdown("""___""")

# Optional logo display in the sidebar
logo = 'logo.png'
st.sidebar.image(logo, width=240)

# Data input section by the user in the sidebar
st.sidebar.header(sidebar_header)

# Load CSV file (if the user uploads one)
uploaded_file = st.sidebar.file_uploader(upload_label, type=['csv'])

# Function to create manual input fields (if no CSV is uploaded)
def user_input_features():
    sbp = st.sidebar.slider(sbp_label, 101, 218, 150)  # Systolic blood pressure
    tabacco = st.sidebar.slider(tobacco_label, 0.00, 31.20, 2.00)  # Tobacco use
    ldl = st.sidebar.slider(ldl_label, 0.98, 15.33, 4.34)  # LDL cholesterol
    adiposity = st.sidebar.slider(adiposity_label, 6.64, 42.49, 26.12)  # Adiposity
    family = st.sidebar.selectbox(family_label, family_options)  # Family history
    type = st.sidebar.slider(type_label, 13, 78, 53)  # Type (numeric field)
    obesity = st.sidebar.slider(obesity_label, 14.70, 46.58, 25.80)  # Obesity
    alcohol = st.sidebar.slider(alcohol_label, 0.00, 147.19, 7.51)  # Alcohol consumption
    age = st.sidebar.slider(age_label, 15, 64, 45)  # Age

    # Create a DataFrame with the input data
    data = {'sbp': sbp,
            'Tobacco': tabacco,
            'ldl': ldl,
            'Adiposity': adiposity,
            'Family': family,
            'Type': type,
            'Obesity': obesity,
            'Alcohol': alcohol,
            'Age': age}
    features = pd.DataFrame(data, index=[0])
    return features

# Load input data (from CSV or manually)
if uploaded_file:
    input_df = pd.read_csv(uploaded_file)
else:
    input_df = user_input_features()

# Preprocess input data
input_df = preprocess_input(input_df)

# Display the input data in the interface
st.subheader(subheader_input)
st.write(input_df)

# Load the model and make the prediction
model = load_model()
prediction, prediction_probability = make_prediction(model, input_df)

# Display prediction and probability in the interface
col1, col2 = st.columns(2)
with col1:
    st.subheader(prediction_label)
    st.write(prediction)
    
with col2: 
    st.subheader(probability_label)
    st.write(prediction_probability)

# Show whether the person has heart problems or not according to the prediction
if prediction == 0:
    st.subheader(no_heart_problems_text)
else:
    st.subheader(heart_problems_text)

# Divider
st.markdown("""___""")
