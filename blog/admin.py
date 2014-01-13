from django.contrib import admin
from blog.models import Category, Entries
from uploads.models import Photo, Album
# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
class EntriesAdmin(admin.ModelAdmin):
    class Media:
        css = {
                "all" : ('css/blogadmin.css', "//code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css",)
                }
        js = ('//code.jquery.com/jquery-1.10.1.min.js', '//code.jquery.com/ui/1.10.3/jquery-ui.js', 'js/jquery.textarea.caret.js', 'js/blogadmin.js',)

    list_display = ('title', 'status', 'featured', 'category', 'created', 'updated_at',)
    list_filter = ('status', 'category', 'created',)

    def get_photo_albums(self):
        albums = Album.objects.all()
        return albums

    def change_view(self, request, object_id, extra_context=None):
        my_context = {
                'albums' : self.get_photo_albums(),
                }
        return super(EntriesAdmin, self).change_view(request, object_id, extra_context=my_context)

    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Entries, EntriesAdmin)
