from django.db import models
from categories.models import Category
# libraries
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Establishment(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True) 
  # location = models.PointField()
  address = models.CharField(max_length=255)
  website = models.CharField(max_length=255, blank=True, null=True)
  phone_number = PhoneNumberField(blank=True)
  email = models.EmailField(blank=True, null=True)
  image = models.ImageField(upload_to="media", blank=True, null=True)
  # is_featured = models.BooleanField(default = False)
  # fk for the apps
  category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

  def __str__(self):
    return self.name