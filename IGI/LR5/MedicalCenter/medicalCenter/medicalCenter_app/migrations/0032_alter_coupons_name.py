# Generated by Django 5.0.4 on 2024-05-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalCenter_app', '0031_remove_coupons_coupon_coupons_name_delete_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupons',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
