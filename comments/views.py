from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm, Comment
from products.models import Product


@login_required
def add_comment(request, product_id):
    """Add comment to specific post. Ensures user is auth'd to do so."""

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.product = get_object_or_404(Product, pk=product_id)
            form.save()

            return redirect('product_view', product_id)

        if len(request.POST['content']) > 500:
            messages.add_message(request, messages.WARNING,
                                 'Comment cannot exceed 500 characters.')

            return redirect('product_view', product_id)

    messages.add_message(request, messages.WARNING,
                         'Error. Something went wrong with your request.')

    return redirect('home')


@login_required
def delete_comment(request, comment_id):
    """Delete comment from specific post. Ensures user is auth'd to do so."""

    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_id)
        url = request.POST['redirect_url']

        if request.user == comment.author:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, 'Comment deleted.')

            return redirect(url)

    messages.add_message(request, messages.WARNING,
                         'Error. Something went wrong with your request.')

    return redirect('home')


@login_required
def update_comment(request, product_id, comment_id):
    """Edit comment on specific post. Ensures user is auth'd to do so."""

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.author:
        form = CommentForm(instance=comment)

        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)

            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Comment updated.')

                return redirect('product_view', product_id)

            if len(request.POST['content']) > 500:
                messages.add_message(request, messages.WARNING,
                                     'Comment cannot exceed 500 characters.')

                return redirect('product_view', product_id)

        context = {'form': form, 'product_id': product_id, }

        return render(request, 'comments/update_comment.html', context)

    messages.add_message(request, messages.WARNING,
                         'Error. Something went wrong with your request.')

    return redirect('home')
