import datetime
import dill

from django.shortcuts import render, redirect
from BloodDonation.confirmations_controller import confirm_donation
from BloodDonation.forms import RequestForm, DonorForm
from BloodDonation.models import Donor, Request
from django.http import HttpResponse
from DonationSystem.settings import channel


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
            if datetime.date.today() - donor_data["date_of_birth"] < datetime.timedelta(days=6570) or datetime.date.today() - donor_data["date_of_birth"] > datetime.timedelta(days=23725):
                return render(request=request, template_name="register_donor.html",
                              context={"donor_form": donor_form, "duplicate": False, "phone_error": False,
                                       "too_young": True})
            donor = Donor(**donor_data)
            # todo: verify number if we have time
            donor.save()
        else:
            return render(request=request, template_name="register_donor.html",
                          context={"donor_form": donor_form, "duplicate": False, "phone_error": False,
                                   "too_young": False, "location_empty": True})
    donor_form = DonorForm()
    return render(request=request, template_name="register_donor.html",
                  context={"donor_form": donor_form, "duplicate": False, "phone_error": False, "too_young": False, "location_empty": False})


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


def display_requests(request, message=""):
    requests = Request.objects.all()
    return render(request=request, template_name="display_requests.html", context={"requests": requests, "message": message})
