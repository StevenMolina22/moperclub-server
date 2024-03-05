from django.contrib import admin

# import the database table:
from .models import Establishment

admin.site.register(Establishment)