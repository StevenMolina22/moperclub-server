from rest_framework import serializers
from .models import Product, Tag
# from .serializer import 

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
  tags = TagSerializer()
  class Meta: 
    model = Product
    fields = "__all__"

