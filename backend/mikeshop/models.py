from django.db import models
from django.contrib.auth.models import AbstractUser

# Register your models here.

class User(AbstractUser):
    pass

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    product_image = models.FileField(upload_to='products') 

class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class BasketItem(models.Model):
    id = models.AutoField(primary_key=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def item_price(self):
        return self.product_id.price * self.quantity

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=20, default="")
    address1 = models.CharField("Address line 1", max_length=100, default="")
    address2 = models.CharField("Address line 2", max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    eircode = models.CharField(max_length=10, default="")
    payment_method = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"Order {self.id}"

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return self.customer_name