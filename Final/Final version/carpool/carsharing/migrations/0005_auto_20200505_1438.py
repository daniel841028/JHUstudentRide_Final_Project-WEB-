# Generated by Django 3.0.5 on 2020-05-05 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carsharing', '0004_auto_20200505_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverlist',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
