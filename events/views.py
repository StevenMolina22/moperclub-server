from django.shortcuts import render

# in the projectname/events/views.py file
from rest_framework import viewsets
from .serializer import EventSerializer
from .models import Event

# creates the view for the table records and serializer
class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    # brings all the records of the Table
    queryset = Event.objects.all()