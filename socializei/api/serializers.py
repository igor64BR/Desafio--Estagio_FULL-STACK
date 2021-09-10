from socializei.models import Evento, Organizador
from rest_framework import serializers


class EventoSerializer(serializers.ModelSerializer):

    organizadores = serializers.StringRelatedField(
        many=True,
        read_only=True
    )
    # sucesso = True
    error_messages = []

    class Meta:
        model = Evento
        fields = (
            'id',
            'titulo',
            'inicio',
            'fim',
            'organizadores',
        )


class OrganizadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizador
        fields = (
            'id',
            'nome',
            'sobrenome',
            'evento',
        )
