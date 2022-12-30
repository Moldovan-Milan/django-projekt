# Generated by Django 3.2.16 on 2022-12-29 20:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="A telefonszámnak ebben a formátumban kell lennie '+999999999'.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=250)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('house_number', models.IntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('payment', models.CharField(choices=[('Bankártya', 'Bankártya'), ('Utánvét', 'Utánvét')], max_length=9)),
                ('delivery', models.CharField(choices=[('Posta', 'posta'), ('DPD', 'DPD'), ('GLS', 'GLS')], max_length=5)),
                ('comment', models.TextField(blank=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]