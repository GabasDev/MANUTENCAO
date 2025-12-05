# api/models.py

from django.db import models
import uuid

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # CORREÇÃO FEITA: Removi o 'null=True'. Agora está correto para o SonarQube.
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=255)
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome} em {self.data.strftime('%d/%m/%Y')}"

class Ingresso(models.Model):
    codigo_ingresso = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='ingressos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ingressos')
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ingresso {self.codigo_ingresso} para {self.evento.nome}"

class Notificacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='notificacoes')
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    enviada = models.BooleanField(default=False)

    def __str__(self):
        return f"Notificação para {self.cliente.nome}"