from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    product = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

# def m2m_changed_cart_receiver(sender,instance,action,*args,**kwargs):
#     if action =="post_add" or action =="post_remove" or action == "post_clear":
#         products = instance.products.all()
#         total = 0
#         for x in products:
#             total += x.price
#         if instance.subtotal != total:
#             instance.subtotal = total
#             instance.save()
#
#
# def pre_save_cart_receiver(sender,instance,*srgs,**kwargs):
#    instance.total = instance.subtotal + 10
#
# pre_save.connect(pre_save_cart_receiver,sender=Cart)
