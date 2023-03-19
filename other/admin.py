from django.contrib import admin
from other.models import UserContact, SiteContact, FAQ, AboutEshop

# Register your models here.
admin.site.register(UserContact),
admin.site.register(SiteContact)
admin.site.register(FAQ)
admin.site.register(AboutEshop)