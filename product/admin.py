from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'amount', 'unit', 'brand')
    list_display_links = ('id', 'description')


admin.site.register(Product, ProductAdmin)
