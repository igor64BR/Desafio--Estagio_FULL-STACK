from django.db import models


# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    organizadores = models.TextField()
    inicio = models.IntegerField()
    fim = models.IntegerField()
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
