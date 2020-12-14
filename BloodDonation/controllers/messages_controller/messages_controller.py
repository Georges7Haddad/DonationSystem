import math
import datetime
import dill
import random

from time import sleep
from BloodDonation.models import Donor, Request
from DonationSystem.settings import channel


def get_donors(blood_type, body):
    """
        Get all possible donors sorted based on their distance to the hospital
    """
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(
        blood_type=blood_type, last_time_donated__lt=datetime.date.today() - datetime.timedelta(weeks=13)
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
    ch.basic_ack(delivery_tag=method.delivery_tag)
    random.shuffle(donors)
    start_index = 0
    end_index = 50
    try:
        for wait_time in [1, 5, 7, 10, 15, 20]:  # in minutes
            request = Request.objects.get(pk=request.id)
            for donor in donors[start_index:end_index]:
                if request.users_confirmations > request.units_needed * 5:
                    return
                channel.basic_publish(exchange='', routing_key="messages", body=dill.dumps({"donor": donor, "request": request}))
            start_index = end_index
            end_index += 50
            sleep(wait_time * 60)
    except Request.DoesNotExist:
        return


def consumer_o_neg(ch, method, properties, body):
    """
       Callback to consume requests with blood type: O-
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("O-", body)
    send_messages(request, donors, ch, method)


def consumer_o_pos(ch, method, properties, body):
    """
       Callback to consume requests with blood type: O+
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("O+", body)
    send_messages(request, donors, ch, method)


def consumer_a_neg(ch, method, properties, body):
    """
       Callback to consume requests with blood type: A-
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("A-", body)
    send_messages(request, donors, ch, method)


def consumer_a_pos(ch, method, properties, body):
    """
       Callback to consume requests with blood type: A+
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("A+", body)
    send_messages(request, donors, ch, method)


def consumer_b_neg(ch, method, properties, body):
    """
       Callback to consume requests with blood type: B-
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("B-", body)
    send_messages(request, donors, ch, method)


def consumer_b_pos(ch, method, properties, body):
    """
       Callback to consume requests with blood type: B+
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("B+", body)
    send_messages(request, donors, ch, method)


def consumer_ab_neg(ch, method, properties, body):
    """
       Callback to consume requests with blood type: AB-
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("AB-", body)
    send_messages(request, donors, ch, method)


def consumer_ab_pos(ch, method, properties, body):
    """
       Callback to consume requests with blood type: AB+
       Parameters:
           ch: Queue Channel
           method: Queue Communication Method
           properties: Message properties
           body: Message body
    """
    request, donors = get_donors("AB+", body)
    send_messages(request, donors, ch, method)
