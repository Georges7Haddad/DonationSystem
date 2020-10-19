from django.urls import path

from BloodDonation import views

urlpatterns = [
    path('', views.register_donor),
]
