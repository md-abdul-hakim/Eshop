from django.contrib import admin
from store.models import (
    Category, Product, ProductImages, 
    VariationValue, Banner,
    MyLogo, MyFavicon, Review, Brand
    )

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

admin.site.register(Review)
admin.site.register(Brand)
admin.site.register(Banner)
admin.site.register(MyLogo)
admin.site.register(Category)
admin.site.register(MyFavicon)
admin.site.register(VariationValue)