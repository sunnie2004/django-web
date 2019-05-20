from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    # slug = models.SlugField(default='')


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("product", kwargs={'slug': self.slug})