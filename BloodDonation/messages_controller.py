import math
import datetime
import dill

from django.shortcuts import get_object_or_404
from BloodDonation.models import Donor, Request
# todo: donors that receives the first message should be shuffled everytime
# todo: if 100 donors confirm that they are going, stop sending messages


def get_donors(blood_type, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(
        blood_type=blood_type, can_donate=True, last_time_donated=datetime.date.today() - datetime.timedelta(weeks=13)
    )

    donors = [(
        donor,
        math.sqrt(((request.x_location - donor.x_location) ** 2) + ((request.y_location - donor.y_location) ** 2))
    ) for donor in all_possible_donors]
    donors.sort(key=lambda tup: tup[1])
    return request, donors


def send_messages_o_neg(ch, method, properties, body):
    request, donors = get_donors("O-", body)
    start_index = 0
    end_index = 50
    # for wait_time in [1, 5, 7, 10, 15, 20, 30, 40, 50, 60]: # in minutes
        # start_index += end_index
        # end_index += 50
        # for donors in donors_sets[start_index:end_index]:
        #     try:
        #         request = Request.objects.get(pk=request["id"])
        # todo: send_message(): include message to confirm that they are going or they can send a specific message
        # except BloodDonation.models.Request.DoesNotExist:
        #         return "Request fulfilled"
        # todo: wait(wait_time)

    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_o_pos(ch, method, properties, body):
    request, donors = get_donors("O+", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_a_neg(ch, method, properties, body):
    request, donors = get_donors("A-", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_a_pos(ch, method, properties, body):
    request, donors = get_donors("A+", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_b_neg(ch, method, properties, body):
    request, donors = get_donors("B-", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_b_pos(ch, method, properties, body):
    request, donors = get_donors("B+", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_ab_neg(ch, method, properties, body):
    request, donors = get_donors("AB-", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_messages_ab_pos(ch, method, properties, body):
    request, donors = get_donors("AB+", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
