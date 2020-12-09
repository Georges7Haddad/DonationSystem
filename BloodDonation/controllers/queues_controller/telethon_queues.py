import django
django.setup()

import dill
from DonationSystem.telethon_client import telethon_client
from telethon.tl.functions.contacts import ImportContactsRequest
from DonationSystem.settings import channel


def add_contact(ch, method, properties, body):
    """
       Callback to consume contacts to be added
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    contact = dill.loads(body)
    result = telethon_client(ImportContactsRequest([contact]))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_message(ch, method, properties, body):
    """
       Callback to consume telegram messages to be sent
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    # todo: Improve messages sent
    body = dill.loads(body)
    donor = body["donor"]
    request = body["request"]
    donor_number = "+961" + str(donor[0].phone_number)
    telethon_client.send_message(donor_number, f'Hey {donor[0].first_name}, id: {donor[0].pk}')
    telethon_client.send_message(donor_number, f'Patient {request.id} needs {request.blood_type} blood in {request.hospital}\nIf you can donate please send "Confirmed"\nIf you wish to be removed from our database please send "Unsubscribe"')
    telethon_client.send_message(donor_number, f'Arabic Hey {donor[0].first_name}, id: {donor[0].pk}')
    telethon_client.send_message(donor_number, f'يحتاج المريض {request.id} إلى {request.blood_type} دم {request.hospital} \ n إذا كان بإمكانك التبرع ، فيرجى إرسال "مؤكد" إذا كنت ترغب في الإزالة من قاعدة بياناتنا ، فيرجى إرسال "إلغاء الاشتراك "')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='contacts', on_message_callback=add_contact)
channel.basic_consume(queue='messages', on_message_callback=send_message)
channel.start_consuming()
