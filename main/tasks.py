import feedparser
from bs4 import BeautifulSoup
from datetime import datetime
from main.models import Commits
def update_commits():
        feed = feedparser.parse('https://github.com/Nimmard.atom')
        entries = feed.entries
        for entry in entries[:4]:
            soup = BeautifulSoup(entry.summary)
            if 'octicon-git-commit' in soup.span['class']:
                code = str(soup.code.a),
                
                if not Commits.objects.filter(code=code):
                    addcommit = Commits(
                            date = datetime.strptime(str(soup.time['title']), '%Y-%m-%d %H:%M:%S'),
                            title= str(soup.find_all(class_='title')[0]),
                            code = code,
                            summary = unicode(soup.blockquote.text)
                            )
                    addcommit.save()
                    print "Woo saved!"

