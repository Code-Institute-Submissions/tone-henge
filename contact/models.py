from django.db import models


class UserQuery(models.Model):
    email = models.EmailField()
    query = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'User queries'

    def __str__(self):
        return f'Query from {self.email}'
