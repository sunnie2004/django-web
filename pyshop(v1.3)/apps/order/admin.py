from django.contrib import admin
from .models import OrderProducts, Order
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import render,redirect,get_object_or_404
from django.template.response import TemplateResponse
from django.urls import path

admin.site.site_header = "Candle Shop"
# Register your models here.
def order_paid(modeladmin, request, queryset):   #admin action
    queryset.update(order_status='2')
order_paid.short_description = "Mark selected order paid"

def order_shipping(modeladmin, request, queryset):   #admin action
    queryset.update(order_status='3')
order_shipping.short_description = "Mark selected order shipping"

def order_shipped(modeladmin, request, queryset):   #admin action
    queryset.update(order_status='4')
order_shipped.short_description = "Mark selected order shipped"

def order_complete(modeladmin, request, queryset):   #admin action
    queryset.update(order_status='5')
order_complete.short_description = "Mark selected order completed"

class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    # raw_id_fields = ("product",)   # change from select-box to  an Input widget
    list_display = ['product','price','quantity','subtotal']
    extra = 0  #control show row number


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductsInline,]
    # list_display = ['sid','get_total_quantity','get_total_price']
    # total_quantity = 0
    # for orderlist in OrderProducts.objects.all():
    #     total_quantity += orderlist.quantity

    list_display = ['sid','order_status','detail']

    # list_display_links = ['sid']
    list_filter = ('order_status',)
    list_per_page = 60
    actions = [order_paid,order_shipping,order_shipped,order_complete]

    fields = (('user','email','phone_number'),
              ('addr','city','state','zip_code'),
              ('total_quantity','total_price','total_weight'),
              ('pay_method','order_status','trade_no'))

    def get_urls(self):    #get admin urls
        urls = super(OrderAdmin,self).get_urls()
        # print('urls:{}'.format(urls))
        customer_urls = [
            path('<order_id>/detail/',self.admin_site.admin_view(self.admin_order_detail),name='order_order_order-detail'),
        ]

        return customer_urls + urls

    def admin_order_detail(self,request, order_id):
        order = get_object_or_404(Order, order_id=order_id)
        items = OrderProducts.objects.filter(orderId=order)

        return render(request, 'admin/order/order/detail.html',{'order':order,'items':items})

    # def order_detail(self,obj):
    #     return format_html('<a href="{}">View</a>',reverse('order_detail', args=[obj.order_id]))
    # order_detail.allow_tags = True

    def detail(self, obj):
        return format_html('<a href="{}">View</a>',reverse('admin:order_order_order-detail', args=[obj.order_id]))

    detail.short_description = 'Detail'
    detail.allow_tags = True

admin.site.register(Order,OrderAdmin)
