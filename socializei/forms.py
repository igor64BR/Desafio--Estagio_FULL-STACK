from django import forms

from socializei.models import Evento, Organizador


class OrganizadorForm(forms.ModelForm):

    class Meta:
        model = Organizador
        fields = [
            'nome',
            'sobrenome',
            'evento'
        ]


class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = [
            'titulo',
            'inicio',
            'fim'
        ]
