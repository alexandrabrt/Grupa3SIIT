from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='stergere_puncte')
@stringfilter
def stergere_puncte(string, simbol):
    print(string)
    # return ''.join(string.split('.'))
    return string.replace('.', simbol)