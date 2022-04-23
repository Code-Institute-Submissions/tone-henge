from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label += '*'
        self.fields['content'].widget.attrs.update({'class': 'form-control', })

    class Meta:
        model = Comment
        fields = ['content', ]
