import feedparser
import pytz
from bs4 import BeautifulSoup
from datetime import datetime
from main.models import Commits
def update_commits():
        feed = feedparser.parse('https://github.com/Nimmard.atom')
        entries = feed.entries
        for entry in entries:
            soup = BeautifulSoup(entry.summary)
            if 'octicon-git-commit' in soup.span['class']:
                code = str(soup.code.a)
                
                print code
                if not Commits.objects.filter(code=code):
                    naivedate = datetime.strptime(str(soup.time['title']), '%Y-%m-%d %H:%M:%S')
                    tzdate = naivedate.replace(tzinfo=pytz.utc)
                    addcommit = Commits(
                            date = tzdate,
                            title= str(soup.find_all(class_='title')[0]),
                            code = code,
                            summary = unicode(soup.blockquote.text)
                            )
                    addcommit.save()
                    print "Woo saved!"

