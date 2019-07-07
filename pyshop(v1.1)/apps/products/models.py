from django.conf import settings
from django.db import models
from db.base_model import BaseModel

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=255,verbose_name='product_name')
    description = models.TextField(default="",verbose_name='description')
    price = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='price')
    image = models.ImageField(upload_to='.',verbose_name='picture',blank=True)
    unit = models.CharField(max_length=20,default=1,verbose_name='unit')
    stock = models.IntegerField(default=1,verbose_name='stock')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = verbose_name
        ordering = ('name',)


    def __str__(self):
        return self.name
