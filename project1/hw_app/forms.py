from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    amount = forms.IntegerField(label='Количество')
    image = forms.ImageField(label='Изображение', required=False)


class ImageForm(forms.Form):
    image=forms.ImageField()