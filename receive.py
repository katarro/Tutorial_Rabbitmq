import pika

# RabbitMQ localmente 
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# RabbitMQ en un contenedor
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))

# Crear un canal. 
channel = connection.channel()

# Asegurarse de que la cola 'hello' exista. Si no existe, RabbitMQ la creará.
channel.queue_declare(queue='hello')

# Función de devolución de llamada que se ejecutará cuando se reciba un mensaje de la cola.
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Indicar a RabbitMQ que queremos consumir mensajes de la cola 'hello' y que, cuando se reciba un mensaje, 
# se debe llamar a la función de devolución de llamada 'callback'.
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# Imprimir un mensaje en la consola para indicar que el programa está esperando mensajes.
print(' [*] Waiting for messages. To exit press CTRL+C')

# Iniciar el bucle de consumo para escuchar mensajes de la cola.
channel.start_consuming()
