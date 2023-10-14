# Utilizar una imagen base de Python 3.8 en su versión "slim"
FROM python:3.8-slim

# Establece el directorio de trabajo /app. 
WORKDIR /app

# Copiar todos los archivos del directorio actual
COPY . .

# Instalar la biblioteca pika usando pip.
RUN pip install pika
