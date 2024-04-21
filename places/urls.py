from django.urls import path, include
from rest_framework import routers
from places import views

router = routers.DefaultRouter()
# table registration
router.register(r'places', views.PlaceView, 'place')

urlpatterns = [
    path("api/", include(router.urls)),
]