from django.test import TestCase

# Create your tests here.
from server.users.models import UserProfile

user1 = UserProfile.objects.get(pk=2)
user1_gender = user1.gender
print(user1_gender)