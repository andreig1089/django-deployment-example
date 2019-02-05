from django import template

register = template.Library()
@register.filter(name='xasdfg')
def xasdfg(value, arg):
    """
    this cuts out all values of arg from string
    """
    return value.replace(arg, '')

#register.filter('xasdfg', xasdfg)
