from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.donations, name='donations'),
    url(r'^donation/new/$', views.donation_new, name='donation_new'),
]