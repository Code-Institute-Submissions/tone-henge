from xml.etree.ElementTree import Comment
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product
from comments.forms import CommentForm, Comment


def products(request):
    """
    Display list of products. Handle sorting method found in URL parameters.
    """

    products = Product.objects.all()
    search_term = None
    sort_method = None
    order = None

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
            sort = sortkey

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'order' in request.GET:
                order = request.GET['order']
                if order == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)
            sort_method = f'{sort}_{order}'

    context = {'products': products, 'search_term': search_term,
               'sort_method': sort_method, }

    return render(request, 'products/products.html', context)


def product_view(request, product_id):
    """
    Render product view template & product comments.
    """

    product = get_object_or_404(Product, pk=product_id)
    form = CommentForm()

    context = {'product': product, 'form': form, }

    return render(request, 'products/product_view.html', context)
