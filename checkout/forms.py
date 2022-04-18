from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone_id', 'country',
                  'postcode', 'city', 'address', 'county']
