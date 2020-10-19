from django.shortcuts import render

from BloodDonation.forms import DonorForm


def register_donor(request):
    if request.method == "POST":
        donor_form = DonorForm(request.POST)
        if donor_form.is_valid():
            first_name = donor_form.cleaned_data["first_name"]
            # todo: add to db

    donor_form = DonorForm()
    return render(request=request, template_name="register_donor.html", context={"donor_form": donor_form})
