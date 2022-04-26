from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserQueryForm
from .models import UserQuery


def contact(request):
    """Render contact page and handle form submission for user queries."""

    if request.method == 'POST':
        form = UserQueryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Thank you. Your query has been \
                sent successfully.')

            return redirect('contact')

        if len(request.POST['query']) > 500:
            messages.add_message(request, messages.WARNING,
                                 'Query cannot exceed 500 characters.')

            return redirect('contact')

    form = UserQueryForm()
    if request.user.is_authenticated:
        form = UserQueryForm(initial={'email': request.user.email})

    context = {'form': form, }

    return render(request, 'contact/contact.html', context)


@login_required
def view_queries(request):
    """Render list of all queries for admin users."""

    if not request.user.is_superuser:
        messages.add_message(request, messages.WARNING,
                             'You do not have permission to do that.')

        return redirect('home')

    queries = reversed(UserQuery.objects.all())
    context = {'queries': queries, }

    return render(request, 'contact/view_queries.html', context)
