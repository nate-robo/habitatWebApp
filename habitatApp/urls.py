from django.conf.urls import url, patterns, include
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.donations, name='donations'),
    url(r'^donation/new/$', views.donation_new, name='donation_new'),
    url(r'^donation/(?P<pk>\d+)/edit/$', views.donation_edit, name='donation_edit'),
    url(r'^donation/(?P<pk>\d+)/$', views.donation_detail, name='donation_detail'),

    url(r'^base$', views.base, name='base'),
    #url(r'^donors$', views.donors, name='donors')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]