# Generated by Django 4.2.11 on 2024-04-05 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0009_alter_book_created_alter_checkout_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 19, 9, 13, 33, 254208, tzinfo=datetime.timezone.utc)),
        ),
    ]
