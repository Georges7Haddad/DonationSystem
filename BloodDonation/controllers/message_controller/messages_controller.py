import math
import datetime
import dill
import random

from BloodDonation.models import Donor, Request

# todo: if 100 donors confirm that they are going, stop sending messages
from DonationSystem.settings import channel


def get_donors(blood_type, body):
    """
        Get all possible donors sorted based on their distance to the hospital
    """
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


def send_messages(request, donors, ch, method):
    # todo: we get all the donors sorted by closest distance then shuffle
    #       we need to find a way to send to closest donors without always starting with the same people
    random.shuffle(donors)
    start_index = 0
    end_index = 50
    try:
        for wait_time in [1, 5, 7, 10, 15, 20, 30, 40, 50, 60]:  # in minutes
            for donor in donors[start_index:end_index]:
                request = Request.objects.get(pk=request.id)
                channel.basic_publish(exchange='', routing_key="messages", body=dill.dumps(donor))
            start_index = end_index
            end_index += 50
            # todo: wait(wait_time)
    except Request.DoesNotExist:
        ch.basic_ack(delivery_tag=method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consumer_o_neg(ch, method, properties, body):
    request, donors = get_donors("O-", body)
    send_messages(request, donors, ch, method)


def consumer_o_pos(ch, method, properties, body):
    request, donors = get_donors("O+", body)
    send_messages(request, donors, ch, method)


def consumer_a_neg(ch, method, properties, body):
    request, donors = get_donors("A-", body)
    send_messages(request, donors, ch, method)


def consumer_a_pos(ch, method, properties, body):
    request, donors = get_donors("A+", body)
    send_messages(request, donors, ch, method)


def consumer_b_neg(ch, method, properties, body):
    request, donors = get_donors("B-", body)
    send_messages(request, donors, ch, method)


def consumer_b_pos(ch, method, properties, body):
    request, donors = get_donors("B+", body)
    send_messages(request, donors, ch, method)


def consumer_ab_neg(ch, method, properties, body):
    request, donors = get_donors("AB-", body)
    send_messages(request, donors, ch, method)


def consumer_ab_pos(ch, method, properties, body):
    request, donors = get_donors("AB+", body)
    send_messages(request, donors, ch, method)
