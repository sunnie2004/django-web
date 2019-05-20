from django.conf import settings
from django.db import models
from products.models import Product

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    item = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.user.username

