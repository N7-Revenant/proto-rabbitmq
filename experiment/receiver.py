#!/usr/bin/env python
import pika
import time


def callback(ch, method, properties, body):

    print(f" [x] Received <{bytes(body).decode()}>")


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.56.81', port=5672,
                                  credentials=pika.credentials.PlainCredentials('test', 'test')))
    channel = connection.channel()

    while True:
        try:
            if channel.is_closed:
                channel = connection.channel()
                print("Channel reopened")

            channel.basic_consume(queue='hello',
                                  auto_ack=True,
                                  on_message_callback=callback)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        except KeyboardInterrupt as exc:
            raise exc

        except Exception as exc:
            print("Error: %s" % type(exc))
            print("Channel closed: %s" % channel.is_closed)
            time.sleep(5)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
