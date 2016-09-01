from django import forms
from .models import Donation, Donor
from django.forms.extras.widgets import SelectDateWidget
from localflavor.us.forms import USPhoneNumberField



# Removes colon associated with label tag
class MySiteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(MySiteForm, self).__init__(*args, **kwargs)


class DonationForm(MySiteForm):
    """Form for adding new donatin to DB"""

    donor = forms.ModelChoiceField(queryset=Donor.objects.all(), widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search':'true', 'data-width':'350px'}))
    date = forms.DateField(widget=SelectDateWidget(attrs={'class':'selectpicker', 'data-width':'114px'}))

     
    class Meta:
        """Form layout"""
        model = Donation
        fields = ('donor', 'date', 'type', 'est_val', 'description')

class DonorForm(MySiteForm):

    cell_phone = USPhoneNumberField(required=False)
    home_phone = USPhoneNumberField(required=False)

    class Meta:
        model = Donor
        fields = ('company', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'home_phone', 'cell_phone', 'email', 'referred_by', 'comments')