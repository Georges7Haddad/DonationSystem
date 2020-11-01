import dill

from django.shortcuts import get_object_or_404

from BloodDonation.models import Donor, Request


def send_messages_o_neg(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")
    # todo: location feature returns sets of donors: should return list of lists
    # Location between donors and request(distance between 2 points with x and y)

    # for donors in donors_sets:
    #     try:
    #         request = get_object_or_404(Request, pk=request["id"])
    #     except:
    #         return "Request fulfilled"

    # todo: send_message()
    # todo: wait()


def send_messages_o_pos(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")


def send_messages_a_neg(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")


def send_messages_a_pos(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")


def send_messages_b_neg(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")


def send_messages_b_pos(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")


def send_messages_ab_neg(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")


def send_messages_ab_pos(ch, method, properties, body):
    request = dill.loads(body)
    all_possible_donors = Donor.objects.filter(blood_type="O-")
