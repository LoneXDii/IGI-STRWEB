# Generated by Django 5.0.4 on 2024-05-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalCenter_app', '0035_schedule_appointment_temp_alter_client_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='temp',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
