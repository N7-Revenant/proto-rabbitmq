#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.81', port=5672,
                              credentials=pika.credentials.PlainCredentials('test', 'test')))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange='',
    routing_key="task_queue",
    body=message.encode(),
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    ))
print(" [x] Sent 'Hello World!'")
connection.close()
