# Usamos una versión ligera de Python
FROM python:3.11-slim

# Definimos la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero la lista de dependencias (optimiza la caché de Docker)
COPY requirements.txt .

# Instalamos las librerías sin guardar caché para mantener la imagen liviana
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el resto del código
COPY . .

# Exponemos el puerto estándar de Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]