from django.db import models


class Donors(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    blood_type = models.CharField(max_length=5)
    location = models.CharField(max_length=26)
    last_time_donated = models.DateField()
    can_donate = models.CharField(max_length=10)

