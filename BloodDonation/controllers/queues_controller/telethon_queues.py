import django
django.setup()

import dill
from DonationSystem.telethon_client import telethon_client
from telethon.tl.functions.contacts import ImportContactsRequest
from DonationSystem.settings import channel


def add_contact(ch, method, properties, body):
    contact = dill.loads(body)
    result = telethon_client(ImportContactsRequest([contact]))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_message(ch, method, properties, body):
    donor = dill.loads(body)
    # todo: add name and hospital
    # telethon_client.send_message("+961" + str(donor[0].phone_number), f'Patient {request.id} needs blood in {hospital}')
    telethon_client.send_message("+961" + str(donor[0].phone_number), 'If you can donate please send "Confirmed"')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='contacts', on_message_callback=add_contact)
channel.basic_consume(queue='messages', on_message_callback=send_message)
channel.start_consuming()
