from django import template
from store.models import MyLogo, MyFavicon

register = template.Library()

@register.filter
def logo(request):
    logo = MyLogo.objects.filter(is_active=True).order_by('id').first()
    if logo:
        return logo.image.url
    else:
        return None

@register.filter
def favicon(request):
    favicon = MyFavicon.objects.filter(is_active=True).order_by('id').first()
    if favicon:
        return favicon.image.url
    else:
        return None