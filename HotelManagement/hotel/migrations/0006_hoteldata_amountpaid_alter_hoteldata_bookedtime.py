# Generated by Django 4.1.7 on 2023-03-02 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_hoteldata_bookedtime_alter_hoteldata_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteldata',
            name='amountpaid',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hoteldata',
            name='bookedtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 2, 10, 56, 52, 99097)),
        ),
    ]
