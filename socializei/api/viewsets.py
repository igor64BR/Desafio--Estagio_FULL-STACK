from ast import Index

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from socializei.api.serializers import EventoSerializer, OrganizadorSerializer
from socializei.models import Evento, Organizador


class EventoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = request.data
        erros = []
        try:
            if '/' in data['inicio'] and '/' in data['fim']:
                inicio = data['inicio'].split('/')
                dia_inicio = int(inicio[0])
                mes_inicio = int(inicio[1])
                ano_inicio = int(inicio[2])

                fim = data['fim'].split('/')
                dia_fim = int(fim[0])
                mes_fim = int(fim[1])
                ano_fim = int(fim[2])

                # Validação de formatação padrão DD/MM/AA
                if not 1 <= dia_inicio <= 31 or \
                        not 1 <= mes_inicio <= 12 or \
                        ano_inicio <= 2020:
                    erros.append('A data inicial deve estar no padrão DD/MM/AAAA e deve ser atual')

                # Check se a dada de inicio é menor que a final no padrão DD/MM/AAAA
                if not 1 <= dia_fim <= 31 or \
                        not 1 <= mes_fim <= 12 or \
                        ano_fim <= 2020:
                    erros.append('A data final deve estar no padrão DD/MM/AAAA e deve ser atual')

                if ano_fim < ano_inicio:
                    erros.append('A data final deve ser maior que a inicial')
                elif ano_fim == ano_inicio:
                    if mes_fim < mes_inicio:
                        erros.append('A data final deve ser maior que a inicial')
                    elif mes_fim == mes_inicio:
                        if dia_fim <= dia_inicio:
                            erros.append('A data final deve ser maior que a inicial')

            else:
                erros.append('Faltam as \'/\' em uma das datas')
        except IndexError:
            erros.append('Faltam campos separados por \'/\'')

        for field in data:
            if data[field] == '':
                erros.append(f'\'{field.title()}\' é campo obrigatório')

        if serializer.is_valid():
            serializer.save()  # salvamento de dados
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            ultimo_criado = Evento.objects.latest('id')  # Pegando o ID do objeto Evento criado

            return Response({
                'sucesso': True,
                'id': ultimo_criado.id
            }, status=status.HTTP_201_CREATED, headers=headers)  # Impressão de validação em JSON na api

        else:
            return Response(data={
                'sucesso': False,
                'errorMessage': erros
            })


class OrganizadorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer
