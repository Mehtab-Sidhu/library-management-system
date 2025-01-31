# Generated by Django 4.2.11 on 2024-04-02 10:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libmgmt', '0004_checkout_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authored', to='libmgmt.author'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libmgmt.book'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 16, 10, 26, 48, 849382, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
