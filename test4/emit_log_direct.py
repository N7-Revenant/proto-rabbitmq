#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.81', port=5672,
                              credentials=pika.credentials.PlainCredentials('test', 'test')))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel. basic_publish(exchange='direct_logs', routing_key=severity, body=message.encode())
print(f" [x] Sent {severity}:{message}")
connection.close()
