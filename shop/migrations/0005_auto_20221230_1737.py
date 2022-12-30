# Generated by Django 3.2.16 on 2022-12-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]