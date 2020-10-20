from django.shortcuts import render

from BloodDonation.forms import DonorForm
from BloodDonation.models import Donor


def register_donor(request):
    if request.method == "POST":
        donor_form = DonorForm(request.POST)
        if donor_form.is_valid():
            donor = Donor(**donor_form.cleaned_data)
            donor.save()

    donor_form = DonorForm()
    return render(request=request, template_name="register_donor.html", context={"donor_form": donor_form})
