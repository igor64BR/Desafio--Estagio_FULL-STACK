from django.contrib import admin
from .models import *


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'organizadores',
        'data_inicio',
        'data_fim',
        # 'url',
        'criado',
        'modificado',
        'ativo'
    )
