# Tutorial RabbitMQ

## 1. Instalación y configuración de RabbitMQ:

1. Descarga la imagen oficial de RabbitMQ desde Docker Hub:
    docker pull rabbitmq:management

2. Ejecuta un contenedor con RabbitMQ:
    docker run -d --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:management

Con esto, se tendrá RabbitMQ corriendo con el plugin de administración. Se puede acceder a la interfaz de administración en http://localhost:15672/ (usuario y contraseña por defecto: guest/guest).


## 2. Uso básico de RabbitMQ:

Para esta demostración, vamos a usar Python y la biblioteca pika.

1. Instala pika (pika proporciona una interfaz para conectar, enviar y recibir mensajes desde y hacia RabbitMQ desde aplicaciones Python.)
    pip install pika

2. Productor: Crea un archivo llamado send.py

3. Consumidor: Crea un archivo llamado receive.py

4. Ejecuta el productor:
    python send.py

5. Ejecuta el consumdir:
    python receive.py

## 3. Dockerización para hacerlo distribuido:

1. Crea un archivo Dockerfile.
2. Construye la imagen:
    docker build -t my-rabbitmq-app .
3.  Ejecuta tu aplicación en un contenedor:
    docker run --link rabbitmq my-rabbitmq-app

