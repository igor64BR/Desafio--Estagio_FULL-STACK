import django.contrib.admindocs.views
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

import eventos.settings
from socializei.forms import OrganizadorForm, EventoForm
from socializei.models import Evento, Organizador


def index(request):
    eventos_itens = Evento.objects.all()
    organizadores_itens = Organizador.objects.all()
    context = {
        'eventos': eventos_itens,
        'organizadores': organizadores_itens,
    }
    return render(request=request, template_name='index.html', context=context)


def organizador_form(request):
    form = OrganizadorForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

    form = OrganizadorForm()
    context = {
        'form': form
    }
    return render(request, 'organizadores.html', context=context)


def evento_form(request):
    form = EventoForm()

    # Validação de campos
    if str(request.method) == 'POST':
        form = EventoForm(request.POST, request.FILES)
        erros = []
        sucesso = True
        if str(request.method) == 'POST':
            titulo = form.data.get('titulo')
            inicio = form.data.get('inicio')
            fim = form.data.get('fim')

            if len(titulo) > 45:
                erros.append('Insira um título de, no máximo 45 caracteres')
            try:
                if '/' in inicio and '/' in fim:
                    inicio = inicio.split('/')
                    dia_inicio = int(inicio[0])
                    mes_inicio = int(inicio[1])
                    ano_inicio = int(inicio[2])

                    fim = fim.split('/')
                    dia_fim = int(fim[0])
                    mes_fim = int(fim[1])
                    ano_fim = int(fim[2])

                    if not 1 <= dia_inicio <= 31 or \
                            not 1 <= mes_inicio <= 12 or \
                            ano_inicio <= 2020:
                        erros.append('A data inicial deve estar no padrão DD/MM/AAAA e deve ser atual')
                        sucesso = False

                    if not 1 <= dia_fim <= 31 or \
                            not 1 <= mes_fim <= 12 or \
                            ano_fim <= 2020:
                        erros.append('A data final deve estar no padrão DD/MM/AAAA e deve ser atual')
                        sucesso = False

                    if ano_fim < ano_inicio:
                        erros.append('A data final deve ser maior que a inicial')
                        sucesso = False

                    elif ano_fim == ano_inicio:
                        if mes_fim < mes_inicio:
                            erros.append('A data final deve ser maior que a inicial')
                            sucesso = False
                        elif mes_fim == mes_inicio:
                            if dia_fim <= dia_inicio:
                                erros.append('A data final deve ser maior que a inicial')
                                sucesso = False
                else:
                    erros.append('Faltam as \'/\' em uma das datas')
                    sucesso = False

            except IndexError:
                erros.append('Faltam campos separados por \'/\'')
                sucesso = False
            except ValueError:
                erros.append('Algo nas suas datas não está certo')
                sucesso = False
            except TypeError:
                erros.append('Favor inserir apenas os números divididos por barras nas datas')

        fim_erros = ''
        for erro in erros:
            if erro != erros[0]:
                fim_erros += f'; {erro}'
            else:
                fim_erros += erro

        if sucesso and form.is_valid():
            form.save()
            form = EventoForm()
            messages.success(request, 'Dados salvos com sucesso!!')
        else:
            messages.error(request, f'ERROR: {fim_erros}')

    context = {
        'form': form,
    }
    return render(request, 'evento.html', context)


def evento_detail(request, pk):
    evento = get_object_or_404(Evento, id=pk)
    todos_organizadores = Organizador.objects.all()
    organizadores = []
    for organizador in todos_organizadores:
        if organizador.evento.id == pk:
            organizadores.append(organizador)
    context = {
        'evento': evento,
        'organizadores': organizadores
    }
    return render(request, 'evento_detail.html', context)


def delete_evento(request, pk):
    evento = get_object_or_404(Evento, id=pk)
    evento.delete()
    eventos_itens = Evento.objects.all()
    organizadores_itens = Organizador.objects.all()
    context = {
        'eventos': eventos_itens,
        'organizadores': organizadores_itens,
    }
    return render(request, 'delete.html', context)


def delete_organizador(request, pk):
    organizador = get_object_or_404(Organizador, id=pk)
    organizador.delete()
    eventos_itens = Evento.objects.all()
    organizadores_itens = Organizador.objects.all()
    context = {
        'eventos': eventos_itens,
        'organizadores': organizadores_itens,
    }
    return render(request, 'delete.html', context)
