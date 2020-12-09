import datetime
from BloodDonation.models import Request, Donor


def confirm_donation(request):
    """
       We substract 1 from the units of blood needed for request with id request_id
       Parameters:
           request (Request): Request which got a donation
   """
    if request.units_needed == 1:
        request.delete()
        return
    request.units_needed = request.units_needed - 1
    request.save()
