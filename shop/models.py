from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_number = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    text = models.TextField()
    price = models.IntegerField()
    is_in_stock = models.BooleanField(default=False)
    size = models.IntegerField()
    rating = models.IntegerField()
    product_image = models.ImageField(upload_to='images/')
    

    def publish(self):
        self.save()

    def get_price(self):
        return self.product.price

    def __str__(self):
        return self.product_name


class Order(models.Model):
    PAYMENTS = (
        ("Bankártya", "Bankártya"),
        ("Utánvét", "Utánvét")
    ) 
    DELIVERYS = (
        ("Posta", "posta"),
        ("DPD", "DPD"),
        ("GLS", "GLS")
    )
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="A telefonszámnak ebben a formátumban kell lennie '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=250)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    house_number = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    payment = models.CharField(choices=PAYMENTS, max_length=9)
    delivery = models.CharField(choices=DELIVERYS, max_length=5)
    comment = models.TextField(blank=True)
    is_delivered = models.BooleanField(default=False)
    order_time = models.DateTimeField(blank=True, null=True)
    price = 0

    def __str__(self):
        return str(self.pk)
