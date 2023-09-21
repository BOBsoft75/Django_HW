from django.core.management.base import BaseCommand
from hw_app.models import Client, Product, Order
from random import randint, uniform, choices
from datetime import date
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Fill db by fake data'

    def handle(self, *args, **options):
        clients = []
        for i in range(5):
            client = Client(name=f'Name{i}',
                            email=f'name{i}@gmail.com',
                            address=f'Address {i}',
                            phone=f'{randint(10000000, 100000000)}')
            client.save()
            clients.append(client)

        products = []
        for i in range(10):
            product = Product(name=f'Product {i}',
                              description='Some description',
                              price=round(uniform(10, 70000), 2),
                              amount=randint(1, 100))
            product.save()
            products.append(product)

        for client in clients:
            for _ in range(20):
                order_products = choices(products, k=3)
                common_price = 0
                for product in order_products:
                    common_price += product.price
                order = Order(client=client, common_price=common_price,
                              date=date(year=2023, month=randint(1, 8), day=randint(1, 26)))
                order.save()
                order.products.set(order_products)
