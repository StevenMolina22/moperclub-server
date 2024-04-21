# project/app/admin.py
from django.contrib import admin
# import the database table:
from .models import UserProfile, Gender, Location

# register the table into the django admin
admin.site.register(UserProfile)
admin.site.register(Gender)
admin.site.register(Location)
