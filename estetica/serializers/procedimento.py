from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField
from estetica.models import Procedimento
from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        imagem_attachment_key = SlugRelatedField(
            source="imagem",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )
        imagem = ImageSerializer(required=False, read_only=True)
        model = Procedimento
        fields= "__all__"

class ProcedimentoListSerializer(ModelSerializer):
    class Meta:
        imagem = SerializerMethodField()
        model = Procedimento
        fields = "__all__"

class ProcedimentoDetailSerializer(ModelSerializer):
    class Meta:
        model = Procedimento
        fields = "__all__"
        depth = 1
