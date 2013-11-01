# Create your views here.
from django.views.generic import TemplateView
import feedparser
from blog.models import Entries
from bs4 import BeautifulSoup
from main.forms import ContactForm
from django.http import HttpResponse
from django.http import Http404
class SiteIndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        feed = feedparser.parse('https://github.com/Nimmard.atom')

        entries = feed.entries
        git_commits = []
        for entry in entries[:4]:
            soup = BeautifulSoup(entry.summary)
            if 'octicon-git-commit' in soup.span['class']:
                blah = {
                        'time' : str(soup.time),
                        'title' : str(soup.find_all(class_='title')[0]),
                        'code' : str(soup.code.a),
                        'summary': unicode(soup.blockquote.text)
                        }
                git_commits.append(blah)
        context = super(SiteIndexView, self).get_context_data(**kwargs)
        context['entries'] = Entries.objects.order_by('-created')[:4]
        context['commits'] = git_commits
        return context

def contact(request):
    if request.is_ajax():
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                message = "FORM IS VALID"
                form.save()
            else:
                message =  "Form is INVALID"
        else:
            raise Http404
        return HttpResponse(message)
    else:
        raise Http404
