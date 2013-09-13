# Create your views here.
from django.views.generic import TemplateView
import feedparser
from blog.models import Entries
from bs4 import BeautifulSoup
import requests
from settings import settings

class SiteIndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        username = 'Nimmard'
        personal_token = settings.GITHUB_PERSONAL_TOKEN
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
        context['github_user'] = requests.get('https://api.github.com/user', auth=(username, personal_token)).json()
        context['github_repos'] = requests.get('https://api.github.com/users/Nimmard/repos', auth=(username, personal_token)).json()
        return context
