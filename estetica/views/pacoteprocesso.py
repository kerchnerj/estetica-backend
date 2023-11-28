from rest_framework.viewsets import ModelViewSet
from estetica.models import PacotesProcesso
from estetica.serializers import PacotesProcessoSerializer


class PacotesProcessoViewSet(ModelViewSet):
    queryset = PacotesProcesso.objects.all()
    serializer_class = PacotesProcessoSerializer