from django.contrib import admin
from .models import *


admin.site.register(Evento)
# @admin.register(Evento)
# class EventoAdmin(admin.ModelAdmin):
#     list_display = (
#         'titulo',
#         'inicio',
#         'fim',
#     )


@admin.register(Organizador)
class OrganizadorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'sobrenome',
        'evento',
    )
