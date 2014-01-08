from django.conf.urls import patterns, url
from uploads.views import GetAlbumList, GetSingleAlbum

urlpatterns= patterns('',
        url(r'^albums/$', GetAlbumList.as_view(), name="albums"),
        url(r'^album/(?P<album_id>\d{3})/$', GetSingleAlbum.as_view(), name="singlealbum"),
        )
