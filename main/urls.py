from django.conf.urls import patterns, url
from main.views import SiteIndexView
urlpatterns = patterns('',
        url(r'$', SiteIndexView.as_view(), name="siteindex"),
        )
