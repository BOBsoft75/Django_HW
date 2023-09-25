from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


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
    # Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    image = models.ImageField(null=True)
    added_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Product name: {self.name}, description:{self.description}, price: {self.price}, amount: {self.amount}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    common_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'Client: {self.client}, product:{self.products}, common_price: {self.common_price}, date: {self.date}'
