from datetime import datetime

from django.db import models


class Donor(models.Model):
    BLOOD_TYPE_CHOICES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    )
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    location = models.CharField(max_length=26)
    last_time_donated = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    can_donate = models.BooleanField(default=True)
