from django.contrib import admin
from parking.models import User, ParkingSlot, Location, Booking

# Register your models here.

admin.site.register(User)
admin.site.register(ParkingSlot)
admin.site.register(Location)
admin.site.register(Booking)
