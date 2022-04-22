from rest_framework.serializers import ModelSerializer
from base.models import Items


class ItemsSerializers(ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
