#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.81', port=5672,
                              credentials=pika.credentials.PlainCredentials('test', 'test')))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
