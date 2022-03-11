from django import template
from women.models import *

register = template.Library()


@register.simple_tag()
def get_categories(filtered=None):
    if not filtered:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filtered)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cats_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cats_selected}
