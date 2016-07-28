from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.donations, name='donations'),
    url(r'^donation/new/$', views.donation_new, name='donation_new'),
    url(r'^donation/(?P<pk>\d+)/edit/$', views.donation_edit, name='donation_edit'),
    url(r'^donation/(?P<pk>\d+)/$', views.donation_detail, name='donation_detail'),
]