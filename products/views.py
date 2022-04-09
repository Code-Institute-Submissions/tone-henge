from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all()

    context = {'products': products, }

    return render(request, 'products/products.html', context)


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {'product': product, }

    return render(request, 'products/product_view.html', context)