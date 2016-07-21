from django.contrib import admin

from .models import Donor, Donation

admin.site.register(Donor)
admin.site.register(Donation)
# Register your models here.
