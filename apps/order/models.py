from django.db import models
from db.base_model import BaseModel
from apps.products.models import Product
# from django.db.models import F, ExpressionWrapper

# Create your models here.
class Order(BaseModel):

    PAY_METHOD_CHOICES = [
        (1,'PAYPAL'),
        (2,'CREDIT CARD'),
    ]

    ORDER_STATUS_CHOICES = [
        (1,'NOT PAY'),
        (2,'PAID,WAIT FOR SHIPPING'),
        (3,'SHIPPING'),
        (4,'SHIPPED'),
        (5,'COMPLETED'),
    ]

    SHIPPING_METHOD_CHOICES = [
        (1, 'STANDARD'),
        (2, 'PRIORITY'),
    ]

    order_id = models.AutoField(primary_key=True,editable=False,verbose_name='order_id')
    user = models.CharField(max_length=100,verbose_name='user')
    email = models.EmailField(default="",verbose_name='email')
    phone_number = models.CharField(max_length=30,verbose_name='phone')

    addr = models.CharField(max_length=255,verbose_name='address')
    zip_code = models.CharField(max_length=100,verbose_name='zip code')
    city = models.CharField(max_length=100,verbose_name='city',default="")
    state = models.CharField(max_length=100,verbose_name='state')

    shipping_method = models.SmallIntegerField(choices=SHIPPING_METHOD_CHOICES,default=1,verbose_name='shipping_method')
    total_quantity = models.IntegerField(default=0,verbose_name='total_quantity')
    total_weight = models.IntegerField(default=0,verbose_name='total_weight')
    total_price = models.DecimalField(max_digits=9,decimal_places=2,default=0,verbose_name='total_price')
    tax = models.DecimalField(max_digits=9,decimal_places=2,default=0,null=True,verbose_name='tax')
    shipping_fee = models.DecimalField(max_digits=9, decimal_places=2, default=0,verbose_name='shipping_fee')

    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES,default=1,verbose_name='pay_method')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES,default=1,verbose_name='order_status')
    trade_no = models.CharField(max_length=128,default='',verbose_name='trade_number')

    class Meta:
        ordering = ('order_id',)

    @property
    def sid(self):
        return "A%05d" % self.order_id

    def __str__(self):
        return self.sid

    # def get_total_quantity(self):
    #     total_quantity = 0
    #     for orderlist in self.orderitems.all():
    #         total_quantity += orderlist.quantity
    #     return total_quantity
    #
    # def get_total_price(self):
    #     total_price = 0
    #     for orderlist in self.orderitems.all():
    #         total_price += orderlist.subtotal
    #     return total_price


class OrderProducts(BaseModel):

    orderId = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items',verbose_name='order_item')  #7/7/2019 add related_name
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,verbose_name='product',default="")
    quantity = models.PositiveIntegerField(default=1,verbose_name='quantity')
    price = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='price')
    subtotal = models.DecimalField(max_digits=9,decimal_places=2,default=0,verbose_name='subtotal')

    # def __str__(self):
    #     return self.order

    class Meta:
        ordering = ('orderId',)

    # def get_subtotal(self):         #need to fix????
    #     return F(self.price) * F(self.quantity)