from django.db import models
from db.base_model import BaseModel

# Create your models here.
class Shipment(BaseModel):
    SHIPPING_METHOD_CHOICES = [
        (1, 'STANDARD'),
        (2, 'PRIORITY'),
    ]


