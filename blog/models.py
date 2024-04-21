from django.db import models
from users.models import UserProfile 
class Post(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    def __str__(self):
        return self.title
  
class Comment(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    def __str__(self):
        return self.title