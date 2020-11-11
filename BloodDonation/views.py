import dill

from django.shortcuts import render, redirect

from BloodDonation.confirmations_controller import confirm_donation
from BloodDonation.forms import RequestForm, DonorForm
from BloodDonation.models import Donor, Request
from django.http import HttpResponse
from DonationSystem.settings import channel, connection


# TODO:
#       1 - Whatsapp Client and sending one message Karim
#       3 - Processing a request: query for all donors and get numbers for whatsapp Kamil
#       4 - Handling locations Nader


def register_donor(request):
    if request.method == "POST":
        donor_form = DonorForm(request.POST)
        if donor_form.is_valid():
            donor = Donor(**donor_form.cleaned_data)
            donor.save()

    donor_form = DonorForm()
    return render(request=request, template_name="register_donor.html", context={"donor_form": donor_form})


def donation_confirmation(request, int):
    message = confirm_donation(int)
    # TODO: print(message) (with how many units still needed)
    return redirect("/display_requests/")


def confirmation_message_request(request):
    return HttpResponse("Requests have been sent to people who are able to donate.")


def request_form(request):
    if request.method == "POST":
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            request1 = Request(**request_form.cleaned_data)
            request1.save()
            blood_type = request_form.cleaned_data["blood_type"]
            channel.basic_publish(exchange='', routing_key=blood_type, body=dill.dumps(request1))
            connection.close()  # todo: check if needed
    request_form = RequestForm()
    return render(request=request, template_name="request_form.html", context={"request_form": request_form})


def display_requests(request):
    requests = Request.objects.all()
    return render(request=request, template_name="display_requests.html", context={"requests": requests})
