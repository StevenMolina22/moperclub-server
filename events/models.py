from django.db import models
from categories.models import Category

class Event(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
  # location = models.PointField()
  address = models.CharField(max_length=255)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  website = models.URLField(null=True, blank=True)
  phone_number = models.CharField(max_length=255, null=True, blank=True)
  # email = models.ForeignKey
  image = models.ImageField(upload_to="media", null=True, blank=True)
  def __str__(self):
    return self.name