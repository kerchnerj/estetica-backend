from rest_framework.viewsets import ModelViewSet
from estetica.models import Agendamento
from estetica.serializers import AgendamentoSerializer


class AgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer