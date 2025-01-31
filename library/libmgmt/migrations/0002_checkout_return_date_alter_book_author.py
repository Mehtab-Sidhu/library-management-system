# Generated by Django 4.2.11 on 2024-04-01 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored', to='libmgmt.author'),
        ),
    ]
