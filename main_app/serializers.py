from rest_framework.serializers import ModelSerializer
from .models import *


class PaintingsSerializer(ModelSerializer):
    class Meta:
        model = Paintings
        fields = '__all__'
