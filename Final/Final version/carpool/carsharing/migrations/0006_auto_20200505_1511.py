# Generated by Django 3.0.5 on 2020-05-05 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsharing', '0005_auto_20200505_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverlist',
            name='email',
        ),
        migrations.RemoveField(
            model_name='driverlist',
            name='name',
        ),
        migrations.AddField(
            model_name='driverlist',
            name='driver',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='carsharing.User'),
            preserve_default=False,
        ),
    ]
