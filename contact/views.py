from django.shortcuts import redirect, render
from .forms import UserQueryForm
from django.contrib import messages


def contact(request):
    """Render contact page and handle form submission for user queries."""

    form = UserQueryForm()

    if request.method == 'POST':
        form = UserQueryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Thank you. Your query has been sent successfully.')

            return redirect('contact')

    context = {'form': form, }

    return render(request, 'contact/contact.html', context)
