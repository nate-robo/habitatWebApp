"""Django Models for DB creation, creates MySQL DB Schema from classes"""

from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
import uuid

''' Donor DB model to create SQL table, one to many relationship with
    donations model '''


class Donor(models.Model):
    """Donor database model"""

    company = models.CharField(max_length=254, blank=True)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    street_address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    home_phone = models.IntegerField(blank=True)
    cell_phone = models.IntegerField(blank=True)
    email = models.EmailField()
    reffered_by = models.CharField(max_length=254, blank=True)
    comments = models.TextField(blank=True)

    def add_donor(self):
        """Add donor to DB"""
        self.save()

    def __str__(self):
        """Return title for DB label"""
        return "Donor " + str(self.id)

    @property
    def get_title(self):
        """Return a title to be used for label in front end"""
        if self.first_name is not '' or self.last_name is not '':
            return self.first_name + ' 1 ' + self.last_name
        elif self.company is not '':
            return self.company
        else:
            return 'Donor ' + str(self.id)

    def get_admin_url(self):
        """Return url for admin portal access"""
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args(self.pk,))

''' Donation DB model to create SQL table, many to one relationship with
    Donor model. '''


class Donation(models.Model):
    """Donation database model"""

    id = models.UUIDField('Donation ID', primary_key=True, default=uuid.uuid4, editable=False)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    date = models.DateField()  # Suspect, working as intended?
    type = models.CharField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    est_val = models.DecimalField('Estimated Value', max_digits=19, decimal_places=2)

    def __str__(self):
        """Return title for DB label"""
        return "Donation " + str(self.id)

    def get_admin_url(self):
        """Return url for admin portal access"""
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args(self.pk,))
