from django.contrib.auth.models import User 
from django.db.models.signals import post_save, post_delete # give a signal when an instance is saved
from django.dispatch import receiver

from .models import UserProfile, Location

# Creates Profile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User) # recommended line, but not needed
    
# Deletes Profile when User is deleted
@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    instance.userprofile.delete()

# Creates Location when Profile is created
@receiver (post_save, sender=UserProfile)
def create_location(sender, instance, created, **kwargs):
    if created:
        Location.objects.create(userprofile=instance)

@receiver(post_delete, sender=UserProfile)
def delete_location(sender, instance, **kwargs):
    try:
        location = instance.location
        if location:
            location.delete()
    except Location.DoesNotExist:
        pass