# Generated by Django 4.2.3 on 2023-07-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_rename_booking_date_booking_reservation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]
