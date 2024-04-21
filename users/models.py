from django.db import models
from django.contrib.auth.models import User
from django import forms 
# libraries and utilities

class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
  

class Location(models.Model):
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=128, blank=True)
    province = models.CharField(max_length=128, blank=True)
    zip_code = models.CharField(max_length=8, blank=True)
    
    def __str__(self):
        return self.userprofile


# Create new table
class UserProfile(models.Model):
    # basic info
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # connection to users module
    address = models.CharField(max_length=255, blank=True)
    gender =  models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL, default=None, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True)
    # --dates
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now = True)
    # --foreign keys to other apps
    location = models.OneToOneField(Location, null=True, on_delete=models.SET_NULL, default=None)

    # Put username as the identifier on the admin page
    def __str__(self):
        return self.user.username
  
