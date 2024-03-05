from django.urls import path, include
from rest_framework import routers
from categories import views

router = routers.DefaultRouter()

router.register(r'categories', views.CategoryView, 'categories')

urlpatterns = [
  path('api/', include(router.urls))
]