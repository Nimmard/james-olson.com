from blog.models import Entries
from django.views.generic import ListView, DetailView
from django.views.generic.dates import MonthArchiveView,YearArchiveView


class BlogDetailView(DetailView):
    model = Entries
    context_object_name = "entry"

class BlogListView(ListView):
    template_name="blog/blog_list.html"
    model = Entries
    context_object_name = "entries"

class CategoryListView(ListView):
    template_name="blog/blog_list.html"
    context_object_name = "entries"
    model = Entries

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context[self.context_object_name] = self.model.objects.filter(category__slug=self.kwargs['slug'])
         
        return context

class EntriesYearArchiveView(YearArchiveView):
    queryset = Entries.objects.all()
    date_field = "created"
    make_object_list = True
    allow_future = True
    context_object_name = "entries"
    template_name = "blog/blog_list.html"

class EntriesMonthArchiveView(MonthArchiveView):
    queryset = Entries.objects.all()
    date_field = "created"
    make_object_list = True
    allow_future = True
    context_object_name = "entries"
    template_name = "blog/blog_list.html"
    month_format = "%B"