# Generated by Django 3.0.5 on 2020-04-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsharing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('location', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['c_time'],
            },
        ),
    ]
