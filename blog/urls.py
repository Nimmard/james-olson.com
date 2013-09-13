from django.conf.urls import patterns, url
from blog.views import BlogListView, EntriesMonthArchiveView, EntriesYearArchiveView, BlogDetailView, CategoryListView
urlpatterns = patterns('',
#        url(r'(?P<pk>[0-9]+)/$', BlogDetail.as_view()),
#        url(r'^$', BlogList.as_view()),
#        url(r'categories/', CategoryList.as_view()),
        url(r'^$', BlogListView.as_view(), name="blogindex"),
        url(r'^(?P<year>\d{4})/$', EntriesYearArchiveView.as_view()),
        url(r'^(?P<year>\d{4})/(?P<month>[-\w]+)/$', EntriesMonthArchiveView.as_view()),
        url(r'^(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name='entry'),
        url(r'^category/(?P<slug>[-\w]+)/$', CategoryListView.as_view()),
        )
