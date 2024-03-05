from rest_framework import serializers
from .models import Establishment

class EstablishmentSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Establishment
    fields = "__all__"