# Generated by Django 3.2.16 on 2022-12-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
