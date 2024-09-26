![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://arielayala-heart-disease-prediction-python-app-streamlit-rtie9k.streamlit.app/)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pickle](https://img.shields.io/badge/Pickle-FFCA28?style=for-the-badge&logo=python&logoColor=black)

# Predicción de Enfermedades del Corazón

## Descripción del Proyecto

Este proyecto tiene como objetivo predecir la presencia de enfermedades del corazón en pacientes utilizando técnicas de aprendizaje automático. Se basa en un conjunto de datos que incluye diversas características de salud y está implementado utilizando Python y bibliotecas populares como Pandas, Scikit-learn y Matplotlib.

Puedes ver una demo [aquí](https://arielayala-heart-disease-prediction-python-app-streamlit-rtie9k.streamlit.app/)

## Funcionalidades

- Predicción de enfermedades cardíacas.
- Visualización de datos.
- Modelos de aprendizaje automático implementados.
- Evaluación del rendimiento del modelo.

## Tecnologías Utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Pickle**

## Instalación

## Uso

Clona el repositorio:
```bash
git clone https://github.com/ArielAyala/heart-disease-prediction-python.git
```

Navega al directorio del proyecto:
```bash
cd heart-disease-prediction-python
```

Crea un entorno virtual:
```bash
python -m venv venv
```

Activa el entorno virtual:
- Windows: ```venv\Scripts\activate```
- Linux/macOS: ```source venv/bin/activate```

Para instalar las dependencias necesarias, ejecuta el siguiente comando (asegúrate de tener Python y pip instalados en tu sistema):
```bash
pip install -r requirements.txt
```

Ejecuta la aplicación:
```bash
streamlit run app-streamlit.py
```

### Usando Docker
También puedes ejecutar la aplicación usando Docker. Tienes un archivo ```Dockerfile```, ```docker-compose.yml```, y ```.dockerignore``` en la raíz de tu proyecto.
Construye y ejecuta la imagen de Docker:
```bash
docker-compose up -d
```

