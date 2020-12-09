import datetime
from BloodDonation.models import Request, Donor


def confirm_donation(request, donor):
    """
       We substract 1 from the units of blood needed for request with id request_id
       We also set the last_time_donated of a user to today
       Parameters:
           donor_id (int): Id of the user who donated
           request_id (int): Id of the request which got a donation
   """
    donor.last_time_donated = datetime.date.today()
    donor.save()
    if request.units_needed == 1:
        request.delete()
        return
    request.units_needed = request.units_needed - 1
    request.save()
