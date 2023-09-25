from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    reg_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'User name: {self.name}, email:{self.email}, phone: {self.phone}, address: {self.address}, registration date: {self.reg_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    image = models.ImageField(null=True)
    added_at = models.DateField(auto_now=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    common_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
