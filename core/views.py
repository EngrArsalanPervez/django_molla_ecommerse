from django.shortcuts import render
from products.models import Categories, Products


def index(request):
    categories = Categories.objects.all()
    products = Products.objects.all()[0:1]
    context = {
        'categories':   categories,
        'products':     products,
    }
    return render(request, 'core/index.html', context)
