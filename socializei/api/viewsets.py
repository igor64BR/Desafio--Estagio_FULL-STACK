import rest_framework.permissions
from rest_framework import viewsets, mixins

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
    # permission_classes = (rest_framework.permissions.IsAuthenticatedOrReadOnly, )


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
    # permission_classes = (rest_framework.permissions.IsAuthenticatedOrReadOnly, )

