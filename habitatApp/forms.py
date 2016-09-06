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

    type = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' Computer'}))
    est_val = forms.DecimalField(label='Estimated Value', required=False, widget=forms.TextInput(attrs={'placeholder':' 30.00'}))
    description = forms.Textarea(attrs={'placeholder': 'Old Apple Computer, Working'})
    class Meta:
        """Form layout"""
        model = Donation
        fields = ('donor', 'date', 'type', 'est_val', 'description')

class DonorForm(MySiteForm):

    cell_phone = USPhoneNumberField(required=False, widget=forms.TextInput(attrs={'placeholder': ' 610-555-5555'}))
    home_phone = USPhoneNumberField(required=False, widget=forms.TextInput(attrs={'placeholder': ' 610-555-5555'}))

    company = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' Lowes'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' John'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' Doe'}))
    street_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' 123 Restore Lane'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Allentown'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' PA'}))
    zip_code = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': ' 18015'})) 
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' donor@restore.com'}))

    class Meta:
        model = Donor
        fields = ('company', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'home_phone', 'cell_phone', 'email', 'referred_by', 'comments')