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

    donor = forms.ModelMultipleChoiceField(queryset=Donor.objects.all())
    date = forms.DateField(widget=SelectDateWidget())
    class Meta:
        """Form layout"""

        model = Donation
        fields = ('donor', 'date', 'type', 'est_val', 'description')


class DonorForm(MySiteForm):

    cell_phone = USPhoneNumberField()
    home_phone = USPhoneNumberField()

    class Meta:
        model = Donor
        fields = ('company', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'home_phone', 'cell_phone', 'email', 'referred_by', 'comments')