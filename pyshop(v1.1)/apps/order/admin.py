from django.contrib import admin
from .models import OrderProducts, OrderInfo

# Register your models here.
class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    # raw_id_fields = ("product",)   # change from select-box to  an Input widget
    list_display = ['sid','product','price','quantity','subtotal']
    extra = 0  #control show row number


class OrderInfoAdmin(admin.ModelAdmin):
    inlines = [OrderProductsInline,]
    list_display = ['sid',]

admin.site.register(OrderInfo,OrderInfoAdmin)
