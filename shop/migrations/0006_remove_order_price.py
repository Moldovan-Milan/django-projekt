# Generated by Django 3.2.16 on 2022-12-30 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20221230_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
    ]