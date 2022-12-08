from django import template
from my_blog.models import *
from datetime import datetime

register = template.Library()

nav_menu= ['Single Post', 'About Author', 'Contact Us']

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def nav_menu_display():
    return nav_menu

@register.simple_tag()
def how_new(self):
    value = datetime.now()
    return value

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}