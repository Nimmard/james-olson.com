from django import template

register = template.Library()

@register.filter
def shortenEntry(value, post):
    value_list = [str(x) for x in value.split(" ")]
    if len(value) >= 45:
        shortened = ' '.join(value_list[:45]) 
        return shortened + "<a href='%s'>...</a>" % post
    else:
        return value


