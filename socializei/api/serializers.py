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
            'sucesso',
            'organizadores',
        )

    def validate(self, data):  # É neste modelo que será feita a validação de erros
        error_messages = []

        for field in data:
            # print(type(field))
            if data[field] == '':
                self.error_messages.append(f'{field.title()} cannot be blank')
                self.sucesso = False
        # if self.sucesso:
            return data
        else:
            raise serializers.ValidationError(self.error_messages)


class OrganizadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizador
        fields = (
            'id',
            'nome',
            'sobrenome',
            'evento',
        )
