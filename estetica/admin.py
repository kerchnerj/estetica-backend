from django.contrib import admin
from estetica.models import (
    Cliente,
    Agendamento,
    Pacote,
    PacotesProcesso,
    Procedimento,
)

admin.site.register(Cliente)
admin.site.register(Agendamento)
admin.site.register(Pacote)
admin.site.register(PacotesProcesso)
admin.site.register(Procedimento)

