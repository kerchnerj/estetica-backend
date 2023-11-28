from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(("CPF"), max_length=11, blank=True, null=True)
    endereco = models.CharField (("endereço"), max_length=55,blank=True, null=False)
    telefone = models.CharField(("telefone"), max_length=11, blank=True, null=True)
    email = models.EmailField(("e-mail"), unique=True)


    def __str__(self) :
        return self.nome