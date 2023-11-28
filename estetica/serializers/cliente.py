from rest_framework.serializers import ModelSerializer
from estetica.models import Cliente

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields= "__all__"

class ClienteListSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ClienteDetailSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        depth = 1
