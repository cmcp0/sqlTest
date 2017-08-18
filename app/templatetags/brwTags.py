from django import template
from itertools import chain
import logging

register = template.Library()

@register.assignment_tag(takes_context=True)
def getClassName(context, node, *args, **kwargs):
    # logging.error(context)
    return type(node).__name__

@register.assignment_tag(takes_context=True)
def getKeys(context, node, *args, **kwargs):
    #TODO validate related models in orden to complete data to send
    #TODO filter by critical fields as passwords and so on
    var = []
    for f in node[0]._meta.get_fields():
        if f.primary_key:
        #     Str = f.name.title()
        #     Str = Str.replace("_", " ")
            var.append('hidden'+f.name)
        else:
            var.append(f.name.title())
    return var

@register.assignment_tag(takes_context=True)
def getAttr(context, node, *args, **kwargs):
    # return context['forloop']['counter0']
    return getattr(node, (context['key'][0].lower()+context['key'][1:]).replace('hidden', ''))

@register.filter(name='quitar')
def quitar(value, arg):
    return value.replace(arg, '')
