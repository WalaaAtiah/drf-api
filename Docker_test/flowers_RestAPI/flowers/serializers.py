
from rest_framework import serializers

from .models import Flower
class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Flower
        # fields=['id','name', 'owner', 'description'] # specific field
        fields='__all__'