from django.urls import path

from BloodDonation import views

urlpatterns = [
    path('register/', views.register_donor),
    path('request/', views.request_form),
    path('confirmed_donation/<int:int>', views.donation_confirmation),
    path('confirm/request/', views.confirmation_message_request),
    path('display_requests/', views.display_requests),
]
