# api/urls.py

from django.urls import path
from .views import (
    ClienteListCreateView,
    ClienteRetrieveUpdateDestroyView,
    EventoListCreateView,
    EventoRetrieveUpdateDestroyView,
    IngressoListCreateView,
    IngressoRetrieveUpdateDestroyView,
    NotificacaoListCreateView,
    NotificacaoRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Endpoints para Clientes
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view(), name='cliente-detail'),

    # Endpoints para Eventos
    path('eventos/', EventoListCreateView.as_view(), name='evento-list-create'),
    path('eventos/<int:pk>/', EventoRetrieveUpdateDestroyView.as_view(), name='evento-detail'),

    # Endpoints para Ingressos
    path('ingressos/', IngressoListCreateView.as_view(), name='ingresso-list-create'),
    path('ingressos/<int:pk>/', IngressoRetrieveUpdateDestroyView.as_view(), name='ingresso-detail'),

    # Endpoints para Notificações
    path('notificacoes/', NotificacaoListCreateView.as_view(), name='notificacao-list-create'),
    path('notificacoes/<int:pk>/', NotificacaoRetrieveUpdateDestroyView.as_view(), name='notificacao-detail'),
]