from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from uploads.models import Album, Photo
from braces.views import AjaxResponseMixin, JSONResponseMixin

class GetAlbumList(AjaxResponseMixin,JSONResponseMixin,ListView):
    model = Album

    def get_ajax(self, request, *args, **kwargs):
        maindict = {}
        for single in self.get_queryset():
            temp_dict = { single.id: {
                'album' : single.name,
                'image': str(single.get_first_image())
                }
                }
            maindict.update(temp_dict)
        return self.render_json_response(maindict)

class GetSingleAlbum(AjaxResponseMixin, JSONResponseMixin, ListView):
    template_name="uploads/single_album_list.html"

    def get_queryset(self):
        self.album = Photo.objects.filter(album_id=self.kwargs['album_id'])
        return self.album

    def get_ajax(self, request, *args, **kwargs):
        maindict = {}
        for single in self.get_queryset():
            temp_dict = { single.id : {
                'name' : single.name,
                'image' : str(single.image),
                'caption' : single.caption,
                'album' : single.album.id
                }
                }
            maindict.update(temp_dict)
        return self.render_json_response(maindict)
