import dill
from DonationSystem.settings import channel


def neg_O_callback(ch, method, properties, body):
    request = dill.loads(body)
    print(f" [x] Received {body}")


channel.basic_consume(queue='O-', auto_ack=True, on_message_callback=neg_O_callback)
channel.start_consuming()
