from django.db import models


class Base(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    criado = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    modificado = models.DateTimeField(verbose_name='Modificado em', auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Organizador(Base):
    email = models.EmailField(max_length=200)

    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'

    def __str__(self):
        return f'{self.nome}'


class Evento(Base):
    organizadores = models.CharField(verbose_name='Organizadores', max_length=200)
    data_inicio = models.DateField(verbose_name='Início', null=False)
    data_fim = models.DateField(verbose_name='Fim', null=False)
    # url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nome
