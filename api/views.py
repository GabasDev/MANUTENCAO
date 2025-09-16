# api/views.py
from rest_framework import generics
from .models import Cliente, Evento, Ingresso, Notificacao
from .serializers import ClienteSerializer, EventoSerializer, IngressoSerializer, NotificacaoSerializer

# Gerenciar Clientes (Listar e Criar)
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Gerenciar um Cliente específico (Ver, Atualizar, Deletar)
class ClienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Gerenciar Eventos (Listar e Criar)
class EventoListCreateView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

# Gerenciar um Evento específico (Ver, Atualizar, Deletar)
class EventoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

# Gerenciar Ingressos (Listar e Criar)
class IngressoListCreateView(generics.ListCreateAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

# Gerenciar um Ingresso específico (Ver, Atualizar, Deletar)
class IngressoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

# Gerenciar Notificações (Listar e Criar)
class NotificacaoListCreateView(generics.ListCreateAPIView):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer

# Gerenciar uma Notificação específica (Ver, Atualizar, Deletar)
class NotificacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer