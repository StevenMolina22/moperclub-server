from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  icon = models.URLField((""), max_length=200, blank=True, null=True)
  def __str__(self):
    return self.name