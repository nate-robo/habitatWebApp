from django import forms
from .models import Donation, Donor


class DonationForm(forms.ModelForm):
    """Form for adding new donatin to DB"""

    class Meta:
        """Form layout"""

        model = Donation
        fields = ('donor', 'date', 'type', 'description', 'est_val')
