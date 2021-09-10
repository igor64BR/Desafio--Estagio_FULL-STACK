import django.contrib.admindocs.views
from django.contrib import messages
from django.shortcuts import render

from socializei.forms import OrganizadorForm, EventoForm


def index(request):
    form = EventoForm()
    context = {
        'form': form
    }
    return render(request=request, template_name='index.html', context=context)


def organizadores(request):
    form = OrganizadorForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            evento = form.cleaned_data['evento']

    form = OrganizadorForm()
    context = {
        'form': form
    }
    return render(request, 'organizadores.html', context=context)


def evento(request):
    form = EventoForm()
    if str(request.method) == 'POST':
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            inicio = form.cleaned_data['inicio']
            fim = form.cleaned_data['fim']

    form = EventoForm()
    context = {
        'form': form
    }
    return render(request, 'evento.html', context=context)
