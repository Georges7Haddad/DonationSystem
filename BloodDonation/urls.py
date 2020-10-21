from django.urls import path

from BloodDonation import views

urlpatterns = [
    path('', views.register_donor),
    path('request/', views.register_request),
    path('confirm/donor', views.confirmation_message_donor),
    path('confirm/request', views.confirmation_message_request),
]
