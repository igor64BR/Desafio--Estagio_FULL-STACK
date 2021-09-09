from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=45, blank=True)
    inicio = models.CharField(max_length=10, blank=True)  # Data no formato dd/mm/yyyy
    fim = models.CharField(max_length=10, blank=True)
    # Os organizadores serão serializados/apresentados a partir do arquivo serializer.py, dentro do diretório "api"

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo


class Organizador(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    evento = models.ForeignKey(on_delete=models.CASCADE, to=Evento, related_name='organizadores')

    class Meta:
        verbose_name = 'Organzador'
        verbose_name_plural = 'Organizadores'
        unique_together = ['nome', 'sobrenome', 'evento']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
