from rest_framework.viewsets import ModelViewSet

from estetica.models import Procedimento
from estetica.serializers import( ProcedimentoListSerializer, ProcedimentoDetailSerializer, ProcedimentoSerializer)

class ProcedimentoViewSet(ModelViewSet):
    queryset = Procedimento.objects.all()
    serializer_class = {
        "list": ProcedimentoListSerializer,
        "retrieve": ProcedimentoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, ProcedimentoSerializer)