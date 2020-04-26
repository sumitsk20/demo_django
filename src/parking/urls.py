
from django.urls import path
from parking.views import booking_views

urlpatterns = [
path('new-booking',booking_views )
]
