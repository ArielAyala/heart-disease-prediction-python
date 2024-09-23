import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Configurar la pagina de Streamit
st.set_page_config(page_title='Heart disease prediction',
                   layout='centered',
                   initial_sidebar_state='auto')


st.title('App to predict heart disease')
st.markdown("""___""")

logo = 'logo.jpeg'
st.sidebar.image(logo, width=150)

st.sidebar.header('Data entered by the user')

uploaded_file = st.sidebar.file_uploader('Upload the CSV file', type=['csv'])

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        sbp = st.sidebar.slider('Systolic blood pressure', 101, 218, 150)
        tabacco = st.sidebar.slider('Accumulated tobacco (kg)', 0.00, 31.20, 2.00)
        ldl = st.sidebar.slider('Low-density lipoprotein cholesterol', 0.98, 15.33, 4.34)
        adiposity = st.sidebar.slider('Adiposity', 6.64, 42.49, 26.12)
        family = st.sidebar.selectbox('Family history of heart disease', ('Present',  'Abser'))
        type = st.sidebar.slider('Type', 13, 78, 53)
        obesity = st.sidebar.slider('Obesity', 14.70, 46.58, 25.80)
        alcohol = st.sidebar.slider('Current alcohol comsumption', 0.00, 147.19, 7.51)
        age = st.sidebar.slider('Age', 15, 64, 45)

        data  = {'sbp': sbp,
                 'Tobacco': tabacco,
                 'ldl': ldl,
                 'Adiposity': adiposity,
                 'Family': family,
                 'Type': type,
                 'Obesity': obesity,
                 'Alcohol': alcohol,
                 'Age': age
                 }
        # Convertimos el diccionario en un dataframe
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Aplicamos el LabelEncoder para convertir la columna 'Family' en valores numericos
encoder = LabelEncoder()
input_df['Family'] = encoder.fit_transform(input_df['Family'])

# Seleccionamos solo primera fila
input_df = input_df[:1]

st.subheader('Data entered by the user')

if uploaded_file is not None:
    st.write(input_df)
else:
    st.write('Waiting for CSV file to load, currently using example input parameters (shown below)')
    st.write(input_df)

# Cargamos el modelo de clasificacion previamente entrenado
load_clf = pickle.load(open('heart.pkl', 'rb'))

# Aplicamos el modelo para realizar predicciones en base a los datos ingresados
prediction = load_clf.predict(input_df)
prediction_probability = load_clf.predict_proba(input_df)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Prediction')
    st.write(prediction)
    
with col2: 
    st.subheader('Probability of prediction')
    st.write(prediction_probability)
    
if prediction == 0:
    st.subheader('The person has no heart problems')
else:
    st.subheader('The person has heart problems')
    
st.markdown("""___""")
