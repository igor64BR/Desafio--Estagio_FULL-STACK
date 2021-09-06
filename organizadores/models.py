from django.contrib.auth.models import User
from django.db import models


class Organizadore(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario}'
