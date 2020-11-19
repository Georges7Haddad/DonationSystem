from datetime import datetime
from django.db import models

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


class Request(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    date_of_birth = models.DateField()
    phone_number = models.PositiveIntegerField(unique=True)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    longitude = models.FloatField()
    latitude = models.FloatField()
    units_needed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.blood_type} {self.units_needed}"


class Donor(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    date_of_birth = models.DateField()
    phone_number = models.PositiveIntegerField(unique=True)
    email_address = models.EmailField()
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    longitude = models.FloatField()
    latitude = models.FloatField()
    last_time_donated = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    can_donate = models.BooleanField(default=True)

    def __str__(self):
        return f"Donor: {self.first_name} {self.last_name} {self.blood_type}"
