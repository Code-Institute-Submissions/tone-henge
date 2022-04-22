from django.db import models


class UserQuery(models.Model):
    email = models.EmailField()
    query = models.TextField(max_length=300)
