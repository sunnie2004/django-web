from django.db import models
import django.utils.timezone as timezone

class BaseModel(models.Model):
    '''abstract base class'''
    create_time = models.DateTimeField(default=timezone.now,auto_created=True,verbose_name='create_time')
    update_time = models.DateTimeField(auto_now=True,verbose_name='update_time')
    is_delete = models.BooleanField(default=False,verbose_name='delete_tag')

    class Meta:
        abstract = True          ###for the abstract class


