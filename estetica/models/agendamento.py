from django.db import models

from .cliente import Cliente
from .procedimento import Procedimento

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT, null=False, related_name="Agendamento" )
    procedimento = models.ForeignKey(Procedimento,on_delete=models.PROTECT, null=False, related_name="Agendamento")
    data_hora = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    confirmacao = models.CharField(max_length=100)


    def __str__(self) :
        return self.nome
    class Meta:
        verbose_name_plural = "Agendamentos"