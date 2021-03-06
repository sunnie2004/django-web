# Generated by Django 2.1 on 2019-07-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20190710_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='order_status',
            field=models.SmallIntegerField(choices=[(1, 'NOT PAY'), (2, 'PAID,WAIT FOR SHIPPING'), (3, 'SHIPPING'), (4, 'SHIPPED'), (5, 'COMPLETED')], default=1, verbose_name='order_status'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='pay_method',
            field=models.SmallIntegerField(choices=[(1, 'PAYPAL'), (2, 'CREDIT CARD')], default=2, verbose_name='pay_method'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(default='', max_length=128, verbose_name='pay_number'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='total_quantity',
            field=models.IntegerField(default=1, verbose_name='total_quantity'),
        ),
    ]
