from blog.models import Entries, Category
from django.views.generic import ListView, DetailView
from django.views.generic.dates import MonthArchiveView,YearArchiveView
from calendar import month_name

class BlogMenuMixin(object):
    
    def get_blog_archives(self):
        edates = Entries.objects.dates('created', 'month')
        archivedict = dict()
        entries_list = Entries.objects.all()
        for entrydate in edates:
            monthname = month_name[entrydate.month]
            if entrydate.year in archivedict:
                archivedict[entrydate.year].update({ monthname : entries_list.filter(
                    created__year=entrydate.year,
                    created__month=entrydate.month).count()})
            else:
                archivedict[entrydate.year] = {
                        monthname : entries_list.filter(
                            created__year=entrydate.year,
                            created__month=entrydate.month).count()
                            }
        return archivedict
    def get_context_data(self, **kwargs):
        context = super(BlogMenuMixin, self).get_context_data(**kwargs)
        context['categories'] = set(Category.objects.filter(entries__isnull=False))
        context['archives'] = self.get_blog_archives()

        return context

class BlogDetailView(BlogMenuMixin, DetailView):
    model = Entries
    context_object_name = "entry"


class BlogListView(BlogMenuMixin, ListView):
    template_name="blog/blog_list.html"
    queryset = Entries.objects.all().select_related()
    context_object_name = "entries"


class CategoryListView(BlogMenuMixin, ListView):
    template_name="blog/blog_list.html"
    context_object_name = "entries"
    model = Entries

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context[self.context_object_name] = self.model.objects.filter(category__slug=self.kwargs['slug'])
         
        return context

class EntriesYearArchiveView(BlogMenuMixin, YearArchiveView):
    queryset = Entries.objects.all()
    date_field = "created"
    make_object_list = True
    allow_future = True
    context_object_name = "entries"
    template_name = "blog/blog_list.html"

class EntriesMonthArchiveView(BlogMenuMixin, MonthArchiveView):
    queryset = Entries.objects.all()
    date_field = "created"
    make_object_list = True
    allow_future = True
    context_object_name = "entries"
    template_name = "blog/blog_list.html"
    month_format = "%B"
