from django.http import HttpResponse
# get_object_or_404 работает аналогично get,т.е.делает selectз апрос к базе данных.Но если запрос не вернёт строку из таблицы БД,представление отрисует страницу с ошибкой 404.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from hw_app.forms import ImageForm
from django.utils import timezone
from . import models
from . import forms
import logging


logger = logging.getLogger(__name__)


# def index(request):
#     logger.info('Index page accessed')
#     return HttpResponse('Главная страница проекта.')


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 2  # (для теста) при делении на 0 (1 / 0) ошибка
    except Exception as e:
        logger.exception(f'Error in "about" page: {e}')
        return HttpResponse('Oops, somthing went wrong.')
    else:
        logger.info('About page accessed')
        return HttpResponse('About project1')


def index(request):
    return render(request, 'hw_app/base1.html')


def get_all_products(request):
    products = models.Product.objects.all()
    return render(request, 'hw_app/products.html', {'products': products})


def order_view(request):
    if request.GET.get('all_orders'):
        orders = models.Order.objects.all()
    elif request.GET.get('last_7_days'):
        orders = models.Order.objects.filter(
            date__gte=timezone.now() - timezone.timedelta(days=7))
    elif request.GET.get('last_30_days'):
        orders = models.Order.objects.filter(
            date__gte=timezone.now() - timezone.timedelta(days=30))
    elif request.GET.get('last_365_days'):
        orders = models.Order.objects.filter(
            date__gte=timezone.now() - timezone.timedelta(days=365))
    else:
        orders = models.Order.objects.all()
    return render(request, 'hw_app/orders.html', {'orders': orders, 'title': 'Список заказов'})


def clients_view(request):
    clients = models.Client.objects.all()
    return render(request, 'hw_app/clients.html', {'clients': clients, 'title': 'Список клиентов'})


def change_product(request, product_id):
    product = models.Product.objects.filter(pk=product_id).first()
    form = forms.ProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.price = form.cleaned_data['price']
        product.amount = form.cleaned_data['amount']
        product.image = image
        product.save()
        return redirect('products')
    else:
        form = forms.ProductForm(initial={'name': product.name, 'description': product.description,
                                          'price': product.price, 'amount': product.amount, 'image': product.image})

    return render(request, 'hw_app/change_product.html', {'form': form})


def change_client(request, client_id):
    client = models.Client.objects.filter(pk=client_id).first()
    form = forms.ClientForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        client.name = form.cleaned_data['name']
        client.email = form.cleaned_data['email']
        client.phone = form.cleaned_data['phone']
        client.address = form.cleaned_data['address']
        client.reg_date = form.cleaned_data['reg_date']
        client.save()
        return redirect('clients')
    else:
        form = forms.ClientForm(initial={'name': client.name, 'email': client.email,
                                          'phone': client.phone, 'address': client.address, 'reg_date': client.reg_date})

    return render(request, 'hw_app/change_client.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        # request.POST чтобы получить текстовую информацию , request.FILES чтобы получить байты
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()  # FileSystemStorage экземпляр позволяет работать с файлами
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'hw_app/upload_image.html', {'form': form})
