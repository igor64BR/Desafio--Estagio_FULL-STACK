from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=45, blank=True)
    inicio = models.CharField(max_length=10, blank=True)  # Data no formato dd/mm/yyyy
    fim = models.CharField(max_length=10, blank=True)
    # sucesso = models.BooleanField(default=True)
    # Os organizadores serão serializados/apresentados a partir do arquivo serializer.py, dentro do diretório "api"

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo

    # def save(self):
    #     is_ok = True
    #     inicio = self.inicio.split('/')
    #     fim = self.fim.split('/')
    #     inicio = [int(n) for n in inicio]
    #     fim = [int(n) for n in fim]
    #     if (fim[1] >= inicio[1]) and (fim[0] > inicio[0]) and (fim[2] >= inicio[2]):
    #         if 1 <= inicio[0] <= 31:
    #             if 1 <= inicio[1] <= 12:
    #                 print('Tudo ok')
    #             else:
    #                 raise ValueError("Mês inválido")
    #         else:
    #             raise ValueError("Dia inválido")
    #     else:
    #         raise ValueError("Fim deve ser maior que Início")
    #     self.date_error_message()


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
