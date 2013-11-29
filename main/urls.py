from django.conf.urls import patterns, url
from main.views import SiteIndexView, PortfolioView
from main.views import contact
urlpatterns = patterns('',
        url(r'^contact/$', contact, name="contact"),
        url(r'^portfolio/$', PortfolioView.as_view(), name="portfolio"),
        url(r'^$', SiteIndexView.as_view(), name="siteindex"),
        )
