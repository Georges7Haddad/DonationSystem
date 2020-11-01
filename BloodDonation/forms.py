from django import forms

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

CITIES_CHOICES = (
    ("33.893791,35.501778", "Beirut"),
    ("34.0047058,36.2022851", "Baalbek"),
    ("34.552631,36.0698871", "Akkar"),
    ("33.6750714,35.5740904", "Beqaa"),
    ("33.85177,35.4202756", "Mount Lebanon"),
    ("33.3796778,35.4704129", "Nabatieh"),
    ("34.3196628,35.6880946", "North"),
    ("33.3418595,35.0904916", "South"),
)


class DateInput(forms.DateInput):
    input_type = "date"


class DonorForm(forms.Form):
    first_name = forms.CharField(max_length=26, min_length=2)
    last_name = forms.CharField(max_length=26, min_length=2)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    phone_number = forms.IntegerField()
    email_address = forms.EmailField()
    blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES)
    location = forms.ChoiceField(choices=CITIES_CHOICES)

    fields = [
        first_name,
        last_name,
        date_of_birth,
        phone_number,
        email_address,
        blood_type,
        location
    ]


class RequestForm(forms.Form):
    first_name = forms.CharField(max_length=26, min_length=2)
    last_name = forms.CharField(max_length=26, min_length=2)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    phone_number = forms.IntegerField()
    blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES)
    location = forms.ChoiceField(choices=CITIES_CHOICES)
    units_needed = forms.IntegerField()


    fields = [
        first_name,
        last_name,
        date_of_birth,
        phone_number,
        blood_type,
        location,
        units_needed

    ]
