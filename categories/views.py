from rest_framework import viewsets
from .serializer import CategorySerializer
from .models import Category

class CategoryView(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()