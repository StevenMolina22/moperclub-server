from django.db import models
from categories.models import Category
from phonenumber_field.modelfields import PhoneNumberField


# to create a new table
class Place(models.Model):
	# to create the columns headings
  name = models.CharField(max_length=255)
  description = models.TextField()
  is_featured = models.BooleanField(default = False)
  email = models.EmailField(blank=True, null=True)
  # location = models.PointField # for later on 
  address = models.CharField(max_length=255, null=True)
  phone_number = PhoneNumberField(blank=True)
  image = models.ImageField(upload_to="media", blank=True, default=None)
  # disconts = models.ManyToManyRel()
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  is_available = models.BooleanField(default = True)

	# to put the name as the element displayed name
  def __str__(self):
	  return self.name