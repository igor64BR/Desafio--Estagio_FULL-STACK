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
        print(dir(serializer))
        if serializer.is_valid():
            serializer.save()  # salvamento de dados
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'deu certo': 'tudo ok'
            }, status=status.HTTP_201_CREATED, headers=headers)  # Impressão de validação em JSON na api
        else:
            return Response(data={
                'deu ruim': 'Erro'
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
