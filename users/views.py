from rest_framework import viewsets
from .models import UserProfile
from .serializer import UserProfileSerializer
from django.contrib.auth.models import User
from .serializer import UserSerializer
# Validation imports
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    # brings all the records of the Table
    queryset = UserProfile.objects.all()

@api_view(['POST'])
def login(request):
    print(request.data) # dev purposes
    user = get_object_or_404(User, username=request.data['username'])

    # Validate correct password for the user, return error if not valid
    if not user.check_password(request.data['password']):
        return Response({"error": "invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create token if user is valid
    token, created = Token.objects.get_or_create(user=user)
    # Serialize user data to be sent to client
    serializer = UserSerializer(instance=user)

    # Return token
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    print(request.data) # dev purposes
    # Serialized the user info sent in the request
    serializer = UserSerializer(data=request.data)

    # Handle user creation, if request info is valid
    if serializer.is_valid():
        # Create new user with serialized info
        serializer.save()

        # Get created user by username
        user = User.objects.get(username=request.data['username'])

        # Set password for the user
        user.set_password(request.data['password'])

        # Save updated info to the database
        user.save()

        # Create token for valid user
        token = Token.objects.create(user=user)

        # Return token and user info
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def profile(request):
    return Response()