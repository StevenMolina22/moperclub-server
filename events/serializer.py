# in the projectname/appname/serializer.py file

from rest_framework import serializers
from .models import Event

# Table serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        # selects the table to serialize
        model = Event
        # Ways to put the fields:
        fields = "__all__"  # faster way to put the fields