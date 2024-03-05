from rest_framework import viewsets
from .models import UserProfile
from .serializer import UserProfileSerializer

class UserProfileView(viewsets.ModelViewSet):
  serializer_class = UserProfileSerializer
  # brings all the records of the Table
  queryset = UserProfile.objects.all()