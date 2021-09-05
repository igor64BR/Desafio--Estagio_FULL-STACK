from django.db import models
# from organizadores.models import Organizadore


# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    confirmado = models.BooleanField(default=False)
    # data_de_inicio = models.DateTimeField(auto_now_add=False)
    # data_de_fim = models.DateTimeField(auto_now_add=False)
    # orgamizadores = models.ManyToManyField(Organizadore)

    def __str__(self):
        return self.nome
