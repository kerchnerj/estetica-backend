from rest_framework.viewsets import ModelViewSet

from estetica.models import Cliente
from estetica.serializers import( ClienteListSerializer, ClienteDetailSerializer, ClienteSerializer)

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = {
        "list": ClienteListSerializer,
        "retrieve": ClienteDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, ClienteSerializer)