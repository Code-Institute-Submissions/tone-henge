from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    """
    Create form and customise fields to be used in checkout template
    to collect delivery information.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].label += '*'
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['phone_id'].label = 'Phone Number'

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone_id', 'country',
                  'postcode', 'city', 'address', 'county']
