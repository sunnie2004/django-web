from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','unit','image','weight']
    list_filter = ['stock']
    list_editable = ['price','stock','unit']

# admin.site.register(Product,ProductAdmin)




