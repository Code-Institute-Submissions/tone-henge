from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm
from products.models import Product


@login_required
def add_comment(request, product_id):
    """Add comment to specific post."""

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.product = Product.objects.get(pk=product_id)
            form.save()

            return redirect('product_view', product_id)

        if len(request.POST['content']) > 500:
            messages.add_message(request, messages.WARNING,
                                 'Comment cannot exceed 500 characters.')

            return redirect('product_view', product_id)

    messages.add_message(request, messages.WARNING,
                         'Error. Something went wrong with your request.')
    return redirect('home')
