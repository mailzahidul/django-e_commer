from django.contrib import admin
from .models import Product, Category

# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'category']
    list_display_links = ['price']
    list_editable = ['title', 'discount_price', 'category']

admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
