import datetime
from BloodDonation.models import Request, Donor


def confirm_donation(request_id, donor_id):
    request = Request.objects.get(id=request_id)
    donor = Donor.objects.get(id=donor_id)
    donor.last_time_donated = datetime.date.today()
    donor.save()
    if request.units_needed == 1:
        request.delete()
        return
    request.units_needed = request.units_needed - 1
    request.save()
