# project/app/admin.py
from django.contrib import admin
# import the database table:
from .models import Post, Comment

# register the table into the django admin
admin.site.register(Post)
admin.site.register(Comment)