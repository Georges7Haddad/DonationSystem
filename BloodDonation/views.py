from django.shortcuts import render

from BloodDonation.forms import DonorForm
from BloodDonation.models import Donor
from django.http import HttpResponse


def register_donor(request):
    if request.method == "POST":
        donor_form = DonorForm(request.POST)
        if donor_form.is_valid():
            donor = Donor(**donor_form.cleaned_data)
            donor.save()

    donor_form = DonorForm()
    return render(request=request, template_name="register_donor.html", context={"donor_form": donor_form})


def register_request(request):
    return HttpResponse("This link will contain the request form.")


def confirmation_message_donor(request):
    return HttpResponse("Thank you for filling this form.")


def confirmation_message_request(request):
    return HttpResponse("Requests have been sent to people who are able to donate.")
