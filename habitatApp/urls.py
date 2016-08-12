from django.conf.urls import url, patterns, include
from django.conf import settings
from . import views

urlpatterns = [
    # Donations and donation sub views
    url(r'^$', views.donations, name='donations'),
    url(r'^donation/new/$', views.donation_new, name='donation_new'),
    url(r'^donation/(?P<pk>\d+)/edit/$', views.donation_edit, name='donation_edit'),
    url(r'^donation/(?P<pk>\d+)/$', views.donation_detail, name='donation_detail'),
    # Donors and Donor sub views
    url(r'^donors/$', views.donors, name='donors'),
    url(r'^donors/new/$', views.donor_new, name='donor_new'),
    url(r'^donors/(?P<pk>\d+)/$', views.donor_detail, name='donor_detail'),
    url(r'^donors/(?P<pk>\d+)/edit/$', views.donor_edit, name='donor_edit'),
    url(r'^donors/(?P<pk>\d+)/delete/$', views.donor_delete, name='donor_delete'),
    # base template for extending
    url(r'^base$', views.base, name='base'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]