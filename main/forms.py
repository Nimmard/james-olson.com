from django.forms import ModelForm
from main.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
