# Generated by Django 4.2.11 on 2024-04-03 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0006_alter_checkout_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 5, 30, 51, 592983, tzinfo=datetime.timezone.utc)),
        ),
    ]
