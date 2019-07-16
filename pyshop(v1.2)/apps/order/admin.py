from django.contrib import admin
from .models import OrderProducts, OrderInfo
from django.urls import reverse
# Register your models here.


def order_detail(obj):
    return '<a href="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[obj.id]))
order_detail.allow_tags = True

class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    # raw_id_fields = ("product",)   # change from select-box to  an Input widget
    list_display = ['product','price','quantity','subtotal']
    extra = 0  #control show row number


class OrderInfoAdmin(admin.ModelAdmin):
    inlines = [OrderProductsInline,]
    # list_display = ['sid','get_total_quantity','get_total_price']
    # total_quantity = 0
    # for orderlist in OrderProducts.objects.all():
    #     total_quantity += orderlist.quantity

    list_display = ['sid','order_status']

admin.site.register(OrderInfo,OrderInfoAdmin)
