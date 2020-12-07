import datetime
import random
import dill

from django.shortcuts import render, redirect
from BloodDonation.controllers.confirmations_controller import confirm_donation
from BloodDonation.forms import RequestForm, DonorForm, HOSPITAL_CHOICES
from BloodDonation.models import Donor, Request
from django.http import HttpResponse
from DonationSystem.settings import channel
from telethon.tl.types import InputPhoneContact

allowedIps = ["127.0.0.1"]


def allow_by_ip(view_func):
    def authorize(request, *args, **kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in allowedIps:
            return view_func(request, *args, **kwargs)
        return HttpResponse('Invalid Ip Access!')

    return authorize


def register_donor(request):
    if request.method == "POST":
        donor_form = DonorForm(request.POST)
        if donor_form.is_valid():
            donor_data = donor_form.cleaned_data

            # Check Duplicate
            if Donor.objects.filter(phone_number=donor_data["phone_number"]).count() > 0:
                return render(request=request, template_name="register_donor.html",
                              context={"donor_form": donor_form, "duplicate": True, "phone_error": False,
                                       "too_young": False})
            # Check Phone Positive
            if donor_data["phone_number"] < 0:
                return render(request=request, template_name="register_donor.html",
                              context={"donor_form": donor_form, "duplicate": False, "phone_error": True,
                                       "too_young": False})
            # Check Age Between 18 and 65
            if datetime.date.today() - donor_data["date_of_birth"] < datetime.timedelta(
                    days=6570) or datetime.date.today() - donor_data["date_of_birth"] > datetime.timedelta(days=23725):
                return render(request=request, template_name="register_donor.html",
                              context={"donor_form": donor_form, "duplicate": False, "phone_error": False,
                                       "too_young": True})
            donor = Donor(**donor_data)
            # todo: verify number if we have time + webhook for message to remove from DB
            # Add Donor to contacts
            contact = InputPhoneContact(client_id=random.randint(0, 999999), phone="+961" + str(donor_data["phone_number"]),
                                        first_name=donor_data["first_name"], last_name=donor_data["last_name"])
            channel.basic_publish(exchange='', routing_key="contacts", body=dill.dumps(contact))
            donor.save()
        else:
            return render(request=request, template_name="register_donor.html",
                          context={"donor_form": donor_form, "duplicate": False, "phone_error": False,
                                   "too_young": False, "location_empty": True})
    donor_form = DonorForm()
    return render(request=request, template_name="register_donor.html",
                  context={"donor_form": donor_form, "duplicate": False, "phone_error": False, "too_young": False,
                           "location_empty": False})


@allow_by_ip
def request_form(request):
    if request.method == "POST":
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            blood_request = request_form.cleaned_data

            # Check Duplicate
            if Request.objects.filter(phone_number=blood_request["phone_number"]).count() > 0:
                return render(request=request, template_name="request_form.html",
                              context={"request_form": request_form, "duplicate": True, "phone_error": False})

            # Check Phone Positive
            if blood_request["phone_number"] < 0:
                return render(request=request, template_name="request_form.html",
                              context={"request_form": request_form, "duplicate": False, "phone_error": True})

            blood_request["longitude"] = float(blood_request['location'].split(",")[0])
            blood_request["latitude"] = float(blood_request['location'].split(",")[1])
            for hospital in HOSPITAL_CHOICES:
                if blood_request["location"] == hospital[0]:
                    blood_request["hospital"] = hospital[1]
                    break

            del blood_request['location']
            request1 = Request(**blood_request)
            request1.save()
            blood_type = request_form.cleaned_data["blood_type"]
            channel.basic_publish(exchange='', routing_key=blood_type, body=dill.dumps(request1))
            return redirect("/confirm/request/")
    request_form = RequestForm()
    return render(request=request, template_name="request_form.html",
                  context={"request_form": request_form, "duplicate": False, "phone_error": False})


def confirmation_message_request(request):
    return HttpResponse("Requests have been sent to people who are able to donate.")


def donation_confirmation(request, int):
    confirm_donation(int)
    return redirect("/display_requests/")


@allow_by_ip
def display_requests(request, message=""):
    requests = Request.objects.all()
    return render(request=request, template_name="display_requests.html",
                  context={"requests": requests, "message": message})
