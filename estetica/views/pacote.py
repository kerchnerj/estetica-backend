from rest_framework.viewsets import ModelViewSet

from estetica.models import Pacote
from estetica.serializers import( PacoteListSerializer, PacoteDetailSerializer, PacoteSerializer)

class PacoteViewSet(ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = {
        "list": PacoteListSerializer,
        "retrieve": PacoteDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, PacoteSerializer)