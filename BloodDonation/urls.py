from django.urls import path

from BloodDonation import views

urlpatterns = [
    path('', views.view_test),
]
