from django import forms
from django.forms import NumberInput

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

HOSPITAL_CHOICES = (
    ("33.8977754,35.4858408", "AUB Medical Center"),
    ("33.885264,35.515033", "LAU Medical Center-Rizk Hospital"),
    ("33.6788958,35.6240768", "Ain Wzen Hospital"),
    ("34.5499728,36.0777838", "Akkar Rahal Hospital"),
    ("34.3818484,36.4224342", "Al Batoul Hospital"),
    ("33.5476337,35.3835679", "Al Hamshari Hospital"),
    ("33.8578072,35.5230202", "Al Hayat Hospital"),
    ("33.857878,35.4901893", "Al Hikmeh Hospital"),
    ("33.854721,35.8272661", "Al Imam Hospital"),
    ("33.8466536,35.6889025", "Al Jabal Hospital"),
    ("34.4826204,35.9381854", "Al Kheir Hospital"),
    ("33.7724434,35.5418484", "Rafic el Hariri Hospital"),
    ("34.4408659,35.8277245", "Al Mounla Hospital"),
    ("34.4137075,34.2385895", "Al Rahma Hospital"),
    ("34.0266049,36.193428", "Al Rayan Hospital"),
    ("34.421494,35.8246801", "Al Salam Hospital Hopital de la Paix"),
    ("33.7869695,35.4812854", "Al Aaskari Military Hospital"),
    ("34.4435918,35.8319609", "Al Hanan Hospital"),
    ("33.8432248,35.4963923", "Al Rasoul Al AAzam Hospital"),
    ("33.8640228,35.4846324", "Al Zahraa Hospital University Medical Center"),
    ("33.4597435,35.2718728", "Alaa-El-Dine Hospital"),
    ("33.3651692,35.491388", "Alhamid Medical Center - Ghandour Hospital"),
    ("33.5509877,35.3667896", "Aljanoub Hospital"),
    ("33.8990381,35.5710196", "Arz Hospital"),
    ("33.7737067,35.7052131", "Azounieh Hospital"),
    ("33.6786119,35.5723672", "Baakleen Hospital"),
    ("33.8535414,35.5038576", "Bahman Hospital"),
    ("34.251294,35.6639032", "Batroun Hospital"),
    ("33.7830534,35.5211474", "Bchamoun Speciality Hospital"),
    ("33.8725601,35.4896217", "Beirut General Hospital"),
    ("33.8081844,35.8657955", "Bekaa Hospital"),
    ("33.8974488,35.4866666", "Bekhaazi Hospital"),
    ("33.8481359,35.5574475", "Belle Vue Hospital"),
    ("33.8428384,35.506759", "Borj Hospital"),
    ("34.3691573,35.8964588", "Centre Hospitalier du Nord"),
    ("33.8193108,35.8566519", "Chtoura Hospital"),
    ("34.1280804,35.6568095", "CHU Notre Dame de Secours Hospital"),
    ("33.8976758,35.4879979", "Clemenceau Medical Center"),
    ("33.8710961,35.5387443", "Clinique du Levant SM"),
    ("33.5573287,35.375036", "Dalaa Hospital"),
    ("33.9839817,36.1588969", "Dar al Amal Hospital"),
    ("34.0380529,36.1884299", "Dar al hikma Hospital"),
    ("33.7631654,33.5451099", "Dar al Shifa Hospital"),
    ("33.8640228,35.4846324", "Zahraa Hospital"),
    ("33.8681979,35.496447", "Dar al Ajaza al Islamia Hospital "),
    ("33.6298216,35.8017162", "Dr Hamed Farhat Hospital"),
    ("34.2898936,35.9660288", "Ehden Hospital"),
    ("34.4394206,35.8333804", "El Bissar Hospital"),
    ("34.5429083,36.0724105", "El Yousef Hospital Center"),
    ("33.8984932,35.481952", "Fouad Khoury Hospital & Associates SAL"),
    ("33.6185984,35.2331032", "Ghossein Hospital"),
    ("33.5600313,35.373119", "Hammoud Hospital University Medical Center"),
    ("33.9003873,35.5690355", "Haroun Hospital"),
    ("33.5533477,35.367764", "Health Medical Center - Osseiran Hospital"),
    ("33.2819158,35.2206874", "Hiram Hospital"),
    ("33.9324925,35.6732425", "Hopital Beit Chabab"),
    ("33.9072116,35.579406", "Hopital Abou Jaoude"),
    ("34.298747,35.8197141", "Hopital Al Borji"),
    ("34.3487117,35.8356703", "Hopital Al Koura"),
    ("34.4123979,35.8299818", "Hopital Albert Haykel sal"),
    ("33.9298636,35.4856246", "Hopital Dr Toni Nassar Sal"),
    ("33.870436,35.5356489", "Hopital Hayek"),
    ("34.1157654,35.6503275", "Hopital Maritime Jbeil"),
    ("34.5675784,36.2592602", "Hopital Notre Dame de la Paix"),
    ("33.8445373,35.5484962", "Hopital Saint Charles"),
    ("34.1442088,35.6434113", "Hopital Saint-Michel Amchit"),
    ("34.3996849,35.8834705", "Hospital Saydet Zgharta"),
    ("33.8815725,35.5167865", "Hotel Dieu de France Hospital"),
    ("33.8784687,35.5983961", "Hospital Dar Al Rahme"),
    ("34.4422018,35.8301326", "Islamic Hospital"),
    ("33.8937169,35.5283994", "Geitawi Hospital"),
    ("33.5627724,35.3765817", "Kassab Hospital"),
    ("34.0104738,35.6458487", "Kesserwan Medical Center"),
    ("33.4519002,35.0060491", "Kharroubi Hospital"),
    ("33.853022,35.8935237", "Khoury General Hospital"),
    ("33.5560453,35.3716551", "Labib Medical Center"),
    ("33.8720674,35.5328777", "Lebanese Canadian Hospital"),
    ("33.8334374,35.9102933", "Libano-Francais Hospital"),
    ("33.8753065,35.5019065", "Makassed Hospital"),
    ("33.9044961,35.5954444", "Middle East Institute of Health Bsalim"),
    ("33.8597554,35.5258753", "Mount Lebanon Hospital (Jabal Lebnen)"),
    ("33.8968501,35.4845251", "Najjar Hospital"),
    ("34.4319586,35.8304545", "New Mazloum Hospital"),
    ("33.9817009,35.6256007", "Notre Dame du Liban Hospital"),
    ("33.8639244,36.008806", "Rayak Hospital"),
    ("33.8955791,35.5147336", "Rosaire Hospital"),
    ("33.8497491,35.5367326", "Sacre Coeur Hospital"),
    ("33.858142,35.5015892", "Sahel General Hospital"),
    ("33.8601332,35.5021052", "Saint Georges Hospital Hamra"),
    ("33.8872286,35.5287835", "Saint Joseph Hospital"),
    ("33.8455513,35.5242586", "Sainte Therese Hospital"),
    ("33.9150837,35.6084525", "Serhal Hospital"),
    ("33.882044,35.5020466", "Specialized Hospital Haidar and Hajjar"),
    ("33.8369321,35.4941948", "St Georges Hadath Hospital"),
    ("33.7561117,35.6981372", "St Louis Hospital"),
    ("33.7942578,35.8738227", "Taanayel General Hospital"),
    ("33.8409704,35.9035648", "Tal Chiha Hospital"),
    ("33.8969177,35.4896111", "Trad Hospital"),
    ("34.26892,36.3916789", "Universal Hospital"),
    ("33.6116601,35.4955203", "West Bekaa Hospital")
)


class DateInput(forms.DateInput):
    input_type = "date"


class ConfirmationForm(forms.Form):
    donor_id = forms.CharField(max_length=10, min_length=1)
    # request_id = forms.CharField(max_length=10, min_length=1, widget=forms.TextInput(attrs={"readonly": "readonly"}))


class DonorForm(forms.Form):
    first_name = forms.CharField(max_length=26, min_length=2)
    last_name = forms.CharField(max_length=26, min_length=2)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    phone_number = forms.IntegerField()
    email_address = forms.EmailField()
    blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES)
    longitude = forms.FloatField(widget=NumberInput(attrs={'id': 'long', 'readonly': 'readonly'}))
    latitude = forms.FloatField(widget=NumberInput(attrs={'id': 'lat', 'readonly': 'readonly'}))

    fields = [
        first_name,
        last_name,
        date_of_birth,
        phone_number,
        email_address,
        blood_type,
        longitude,
        latitude
    ]


class RequestForm(forms.Form):
    first_name = forms.CharField(max_length=26, min_length=2)
    last_name = forms.CharField(max_length=26, min_length=2)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    phone_number = forms.IntegerField()
    blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES)
    location = forms.ChoiceField(choices=HOSPITAL_CHOICES)
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
