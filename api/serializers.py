# api/serializers.py

from rest_framework import serializers
from .models import Cliente, Evento, Ingresso, Notificacao

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class IngressoSerializer(serializers.ModelSerializer):
    # Usamos os serializers relacionados para mostrar mais detalhes
    cliente = ClienteSerializer(read_only=True)
    evento = EventoSerializer(read_only=True)

    # Campos para criação (apenas IDs)
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), source='cliente', write_only=True)
    evento_id = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all(), source='evento', write_only=True)

    class Meta:
        model = Ingresso
        fields = ['id', 'codigo_ingresso', 'evento', 'cliente', 'data_compra', 'cliente_id', 'evento_id']

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'