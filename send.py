import pika


# RabbitMQ localmente 
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# RabbitMQ en un contenedor
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))

# Crear un canal.
channel = connection.channel()

#  'hello' exista.
channel.queue_declare(queue='hello')

# Enviar un mensaje 'Hello World!' a la cola 'hello'.
# El parámetro 'exchange' está vacío, lo que significa que estamos usando el exchange por defecto de RabbitMQ.
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# Imprimir un mensaje en la consola para confirmar que el mensaje ha sido enviado.
print(" [x] Sent 'Hello World!'")

# Cerrar la conexión con RabbitMQ.
connection.close()
