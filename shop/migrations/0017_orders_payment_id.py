# Generated by Django 3.2 on 2021-04-12 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_orders_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
