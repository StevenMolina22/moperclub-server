from rest_framework import viewsets
from .serializer import PlaceSerializer
from .models import Place

class PlaceView(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()