from django.contrib import admin
from order.models import  Cart, Order, Wish, OrderUpdate

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Wish)
admin.site.register(OrderUpdate)

