from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} @ {self.date}'
