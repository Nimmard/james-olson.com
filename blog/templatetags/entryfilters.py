from django import template
import markdown2
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
register = template.Library()

@register.filter(is_safe=True)
def markdowner(value):
    value = markdown2.markdown(str(value), extras={"html-classes" : {"img" : "testing" } })
    return mark_safe(value)

@register.filter
def shortenEntry(value, post):
    value_list = [str(x) for x in value.split(" ")]
    if len(value) >= 45:
        shortened = ' '.join(value_list[:45]) 
        return shortened + "<a href='%s'>...</a>" % post
    else:
        return value


