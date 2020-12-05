import math
import datetime
import dill
import random

from BloodDonation.models import Donor, Request
from DonationSystem.telethon_settings import telethon_client, start_telethon_client


# todo: if 100 donors confirm that they are going, stop sending messages

start_telethon_client()


def get_donors(blood_type, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(
        blood_type=blood_type, can_donate=True,
        last_time_donated__lt=datetime.date.today() - datetime.timedelta(weeks=13)
    )

    donors = [(
        donor,
        math.sqrt(((request.longitude - donor.longitude) ** 2) + ((request.latitude - donor.latitude) ** 2))
    ) for donor in all_possible_donors]
    donors.sort(key=lambda tup: tup[1])
    return request, donors


def send_messages_o_neg(ch, method, properties, body):
    request, donors = get_donors("O-", body)
    random.shuffle(donors)
    start_index = 0
    end_index = 50
    for wait_time in [1, 5, 7, 10, 15, 20, 30, 40, 50, 60]:  # in minutes
        start_index += end_index
        end_index += 50
        for donor in donors[start_index:end_index]:
            try:
                request = Request.objects.get(pk=request["id"])
                telethon_client.send_message(donor.phone_number,
                                             'Can you please donate blood at this location? if yes type "confirmed"')
            except Request.DoesNotExist:
                return "Request fulfilled"
        # todo: wait(wait_time)

    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_o_pos(ch, method, properties, body):
    request, donors = get_donors("O+", body)
    random.shuffle(donors)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_a_neg(ch, method, properties, body):
    request, donors = get_donors("A-", body)
    random.shuffle(donors)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_a_pos(ch, method, properties, body):
    request, donors = get_donors("A+", body)
    random.shuffle(donors)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_b_neg(ch, method, properties, body):
    request, donors = get_donors("B-", body)
    random.shuffle(donors)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_b_pos(ch, method, properties, body):
    request, donors = get_donors("B+", body)
    random.shuffle(donors)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_ab_neg(ch, method, properties, body):
    request, donors = get_donors("AB-", body)
    random.shuffle(donors)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_ab_pos(ch, method, properties, body):
    request, donors = get_donors("AB+", body)
    random.shuffle(donors)
    ch.basic_ack(delivery_tag=method.delivery_tag)
