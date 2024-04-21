from django.db import models
from users.models import UserProfile

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
class Product(models.Model):
    user_id = models.ManyToManyField(UserProfile, blank=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="media", blank=True, default=None)
    # physical properties
    weight = models.FloatField(blank=True, null=True, default=None)
    height = models.FloatField(blank=True, null=True, default=None)
    length = models.FloatField(blank=True, null=True, default=None)
    width = models.FloatField(blank=True, null=True, default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # fk to other tables
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
  
