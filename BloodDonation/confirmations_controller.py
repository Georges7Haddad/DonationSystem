# TODO: not anyone can submit or confirm requests(only medical staff) if he knows the url (implement password?)
from BloodDonation.models import Request


def confirm_donation(request_id):
    request = Request.objects.get(id=request_id)
    if request.units_needed == 1:
        request.delete()
        return
        # return f"{request.first_name} {request.last_name} does not need anymore units of blood"
    request.units_needed = request.units_needed - 1
    request.save()
    # return f"{request.first_name} {request.last_name} still needs {request.units_needed} units"
