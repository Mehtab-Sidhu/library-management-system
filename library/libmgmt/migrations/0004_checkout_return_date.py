# Generated by Django 4.2.11 on 2024-04-02 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0003_remove_checkout_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 16, 5, 58, 17, 267716, tzinfo=datetime.timezone.utc)),
        ),
    ]
