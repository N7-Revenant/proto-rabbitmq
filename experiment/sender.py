#!/usr/bin/env python
import pika
import time
from pika.exceptions import NackError
from random import randint

QUEUE_NAME = 'hello'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.81', port=5672,
                              credentials=pika.credentials.PlainCredentials('test', 'test')))
channel = connection.channel()

channel.queue_delete(queue=QUEUE_NAME)

channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-length': 30,
    'x-overflow': 'reject-publish'
})

channel.confirm_delivery()

while True:
    try:
        time.sleep(1)
        text = "Hello World %s!" % randint(0, 9)
        channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=text.encode())
        print(" [x] Sent '%s'" % text)

    except KeyboardInterrupt:
        break

    except NackError as exc:
        print('%s' % exc)

    except Exception as exc:
        print("Unable to send message due to exception: %r" % exc)

connection.close()
