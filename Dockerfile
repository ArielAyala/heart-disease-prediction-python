# Utiliza una imagen base de Python con Streamlit preinstalado
FROM python:3.9-slim-buster

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y los demás archivos de la aplicación
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto por defecto de Streamlit (8501)
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "app-streamlit.py"]