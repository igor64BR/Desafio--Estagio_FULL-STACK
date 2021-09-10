from django import forms

from socializei.models import Evento


class EventoForm(forms.Form):
    titulo = forms.CharField(max_length=45)
    inicio = forms.CharField(max_length=10, min_length=10)
    fim = forms.CharField(max_length=10, min_length=10)
    organizadores = forms.ModelChoiceField


class OrganizadorForm(forms.Form):
    eventos = Evento.objects.all()

    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)
    evento = forms.ModelChoiceField(eventos)
