# Generated by Django 5.0.4 on 2024-05-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalCenter_app', '0033_remove_coupons_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='coupon',
            field=models.CharField(default='', max_length=10),
        ),
    ]
