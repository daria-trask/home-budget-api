# Generated by Django 2.0.6 on 2018-06-07 14:23

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('accounts', '0004_auto_20180607_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.RemoveField(
            model_name='list',
            name='account',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
