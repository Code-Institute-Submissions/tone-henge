from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishlistItem
from products.models import Product


@login_required
def wishlist(request):
    """Render user's wishlist page."""

    return render(request, 'wishlist/wishlist.html')


@login_required
def add_to_wishlist(request, product_id):
    """Add item to user's wishlist."""

    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = WishlistItem(user=request.user, product=product)
    wishlist_item.save()

    messages.add_message(request, messages.SUCCESS, 'Added to wishlist.')
    return redirect('product_view', product_id)


@login_required
def remove_from_wishlist(request, product_id):
    """Remove item from user's wishlist"""

    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = request.user.wishlist.get(product=product)
    wishlist_item.delete()

    messages.add_message(request, messages.SUCCESS, 'Removed from wishlist.')
    return redirect('product_view', product_id)
