# Generated by Django 4.2.11 on 2024-04-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0002_checkout_return_date_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='return_date',
        ),
    ]
