from rest_framework import viewsets
from .serializers import EstablishmentSerializer
from .models import Establishment

class EstablishmentView(viewsets.ModelViewSet):
  serializer_class = EstablishmentSerializer
  queryset = Establishment.objects.all()