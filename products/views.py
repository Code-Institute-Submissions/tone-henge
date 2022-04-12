from django.shortcuts import render
from django.db.models import Q
from .models import Product


def products(request):
    products = Product.objects.all()
    search_term = None

    if request.GET:
        if 'q' in request.GET:
            search_term = request.GET['q']

            queries = Q(name__icontains=search_term) | Q(
                content__icontains=search_term) | Q(category__name__icontains=search_term)
            products = products.filter(queries)

        if 'category' in request.GET:
            category = request.GET['category'].replace('+', ' ')
            products = Product.objects.filter(category__name__iexact=category)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'order' in request.GET:
                order = request.GET['order']
                if order == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

    context = {'products': products, 'search_term': search_term, }

    return render(request, 'products/products.html', context)


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {'product': product, }

    return render(request, 'products/product_view.html', context)
