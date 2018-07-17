# Connect to RabbitMQ using pika.BlockingConnection
# This will connect to the virtual host /myvhost
import pika

parameters = pika.URLParameters('amqp://user:passwd@host:5672/%2Fmyvhost')
conn = pika.BlockingConnection(parameters)
conn.close()
