# Create your views here.
from django.views.generic import TemplateView
from blog.models import Entries
from main.forms import ContactForm
from django.http import HttpResponse
from django.http import Http404
from main.models import Commits
from django.core.mail import send_mail, BadHeaderError
class SiteIndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(SiteIndexView, self).get_context_data(**kwargs)
        context['entries'] = Entries.objects.order_by('-created')[:4]
        context['commits'] = Commits.objects.order_by('-date')[:4]
        return context

class PortfolioView(TemplateView):
    template_name = 'main/portfolio.html'

def contact(request):
    if request.is_ajax():
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                name = request.POST.get('name', '')
                subject = "Contact from {0}".format(name)
                from_email = request.POST.get('email', '')
                body = """
                        Name: {0}
                        Phone Number: {1}
                        E-mail: {2}
                        Message: \n {3}""".format(name, 
                                    request.POST.get('phone', ''), from_email,
                                    request.POST.get('message', ''))
                try:
                    send_mail(subject, body, from_email, ['nimmard@gmail.com'])
                    message = "FORM IS VALID"
                except BadHeaderError:
                    message = 'Invalid Header Found'
                form.save()
            else:
                message =  "Form is INVALID"
        else:
            raise Http404
        return HttpResponse(message)
    else:
        raise Http404
