from django.forms import ModelForm
from .models import UserQuery


class UserQueryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].label += '*'

    class Meta:
        model = UserQuery
        fields = ['email', 'query']
