# Connect to RabbitMQ using pika.BlockingConnection and consume messages
import pika


def consumer_callback(ch, method, properties, body):
    ch.basic_ack(method.delivery_tag)
    print(ch, method, properties, body)


parameters = pika.URLParameters('amqp://newsworthy:password1!@127.0.0.1:5672/%2Fnewsworthy')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='newsworthy', exchange_type='fanout')
ret = channel.queue_declare(auto_delete=True)
print(ret)
print(ret.method.queue)
ret2 = channel.queue_bind(ret.method.queue, 'newsworthy')
print(ret2)
channel.basic_consume(consumer_callback, ret.method.queue)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
