from unicodedata import category
from django.shortcuts import render
from django.db.models import Q
from .models import Product


def products(request):
    products = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']

            queries = Q(name__icontains=query) | Q(content__icontains=query) | Q(category__name__icontains=query)
            products = products.filter(queries)

    context = {'products': products, }

    return render(request, 'products/products.html', context)


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {'product': product, }

    return render(request, 'products/product_view.html', context)