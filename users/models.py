from django.db import models
from django.contrib.auth.models import User
# from products.models import Product
# libraries and utilities

class Gender(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
	  return self.name
  
# to create a new table
class UserProfile(models.Model):
  # basic info
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # connection to users module
  address = models.CharField(max_length=255, blank=True)
  gender =  models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL, default=None)
  birth_date = models.DateField(blank=True, null=True)
  phone = models.CharField(max_length=255, blank=True)
  # --dates
  created_at = models.DateField(auto_now_add=True, null=True)
  updated_at = models.DateField(auto_now = True)
  # --foreign keys to other apps

	# to put the title as the element displayed name
  def __str__(self):
	  return self.user.username
  
