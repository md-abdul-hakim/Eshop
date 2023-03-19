from django import template
from order.models import Wish

register = template.Library()

@register.filter
def wish_view(user):
    wish = Wish.objects.filter(user=user)
    if wish:
        return wish
    else:
        return wish

@register.filter
def wish_count(user):
    wish = Wish.objects.filter(user=user)
    if wish:
        return wish.count()
    else:
        return 0