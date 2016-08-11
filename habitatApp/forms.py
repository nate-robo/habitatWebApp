from django import forms
from .models import Donation, Donor
from django.forms.extras.widgets import SelectDateWidget

class DonationForm(forms.ModelForm):
    """Form for adding new donatin to DB"""

    date = forms.DateField(widget=SelectDateWidget())
    class Meta:
        """Form layout"""

        model = Donation
        fields = ('donor', 'date', 'type', 'description', 'est_val')


class DonorForm(forms.ModelForm):

    class Meta:
        model = Donor
        fields = ('company', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'home_phone', 'cell_phone', 'email', 'referred_by', 'comments')