from socializei.models import Evento, Organizador
from rest_framework import serializers


class EventoSerializer(serializers.ModelSerializer):

    organizadores = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Evento
        fields = (
            'id',
            'titulo',
            'inicio',
            'fim',
            'organizadores',
            # 'sucesso'
        )

    def validate(self, data):  # É neste modelo que será feita a validação de erros
        success = True
        print(data)
        error_messages = []
        fields = [e for e in data]
        print(fields)
        for field in fields:
            if len(str(data[field])) == 0:
                success = False
                error_messages.append(f'{field} não pode estar em branco')

        if '/' not in data['inicio'] or data['fim'] or (len(data['inicio']) and len(data['fim']) != 10):
            success = False
            error_messages.append('A data inserida deve ser no padrão DD/MM/YYYY')
        else:
            pass

        if success:
            return data
        else:
            raise serializers.ValidationError(error_messages)


class OrganizadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizador
        fields = (
            'id',
            'nome',
            'sobrenome',
            'evento',
        )
