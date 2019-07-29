# Connect to RabbitMQ using pika.BlockingConnection
# This will connect to the virtual host /myvhost
import pika
import random
import time

parameters = pika.URLParameters('amqp://user:password@127.0.0.1:5672/%2Fmyvhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='myexchange', exchange_type='fanout')

# Turn on delivery confirmations
channel.confirm_delivery()

# Send a message
while True:
    msg = 'Hello, {}'.format(random.randint(0, 100))
    if channel.basic_publish(exchange='myexchange',
                             routing_key='',
                             body=msg,
                             properties=pika.BasicProperties(content_type='text/plain',
                                                             delivery_mode=1)):
        print(msg)
    else:
        print('Message could not be confirmed')
    time.sleep(10)
