from django.shortcuts import render
from parking.forms import BookingForm
from parking.models import Booking


# Create your views here.
def booking_views(request):
    bookin_form = BookingForm()
    context = {"booking_form": bookin_form}
    return render(request, "new_booking.html", context)
