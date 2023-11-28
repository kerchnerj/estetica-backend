from django.db import models


from .pacote import Pacote
from .procedimento import Procedimento


class PacotesProcesso (models.Model):
   pacote = models.ForeignKey(Pacote,on_delete=models.PROTECT, null=False, related_name="PacotesProcesso")
   procedimento = models.ManyToManyField(Procedimento,related_name="+")
   quantidade = models.IntegerField(null=True, default=0)
   

   def __str__(self):
      return self.pacote