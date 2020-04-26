from django import forms
from parking.models import Booking


class BookingForm(forms.ModelForm):
    user_feedback = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Booking
        fields = "__all__"
        # widgets = {
        #     "name": Textarea(attrs={"cols": 80, "rows": 20}),
        # }
