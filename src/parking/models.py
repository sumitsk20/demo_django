from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AbstractTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

    def __str__(self):
        value = self.id
        if hasattr(self, "email"):
            value = self.email
        elif hasattr(self, "number"):
            value = "{0}-{1}".format(self.location.name, str(self.number),)
        elif hasattr(self, "name"):
            value = self.name
        elif hasattr(self, "user"):
            value = "{0}_{1}_{2}".format(
                self.user.username, self.location.name, str(self.slot.number),
            )
        return str(value)


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        value = self.id
        if self.email:
            value = self.email
        return value


class Location(AbstractTimeStampModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)


class ParkingSlot(AbstractTimeStampModel):
    RESERVED = "Reserved"
    AVAILABLE = "Available"
    slot_status = (
        (RESERVED, "Reserved"),
        (AVAILABLE, "Available"),
    )
    status = models.CharField(max_length=50, choices=slot_status, default=AVAILABLE)
    number = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)


class Booking(AbstractTimeStampModel):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    booking_status = (
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (CANCELLED, "Cancelled"),
    )
    user = models.ForeignKey(User, to_field="email", on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=booking_status, default=PENDING)

    booking_date_start = models.DateField(auto_now=False, auto_now_add=False)
    booking_date_end = models.DateField(auto_now=False, auto_now_add=False)
    booking_time_start = models.TimeField(auto_now=False, auto_now_add=False)
    booking_time_end = models.TimeField(auto_now=False, auto_now_add=False)
