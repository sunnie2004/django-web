# Generated by Django 2.1 on 2019-07-08 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190706_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='order.OrderInfo', verbose_name='order'),
        ),
    ]
