# Generated by Django 2.1 on 2019-07-06 21:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, default=django.utils.timezone.now, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='delete_tag')),
                ('name', models.CharField(max_length=255, verbose_name='product_name')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('image', models.ImageField(blank=True, upload_to='.', verbose_name='picture')),
                ('unit', models.CharField(default=1, max_length=20, verbose_name='unit')),
                ('stock', models.IntegerField(default=1, verbose_name='stock')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'product',
                'ordering': ('name',),
            },
        ),
    ]
