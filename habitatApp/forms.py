from django import forms
from .models import Donation, Donor


class DonationForm(forms.ModelForm):
    """Form for adding new donatin to DB"""

    class Meta:
        """Form layout"""

        model = Donation
        widgets = {
        'data': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        fields = ('donor', 'date', 'type', 'description', 'est_val')
