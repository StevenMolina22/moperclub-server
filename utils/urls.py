# projectname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('featured/', views.get_featured_data, name="featured"),
]