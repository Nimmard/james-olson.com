from django.conf.urls import patterns, url
from main.views import SiteIndexView
from main.views import contact
urlpatterns = patterns('',
        url(r'^contact/$', contact, name="contact"),
        url(r'$', SiteIndexView.as_view(), name="siteindex"),
        )
