from django.urls import path, include
from rest_framework import routers
from establishments import views

router = routers.DefaultRouter()

router.register(r'establishments', views.EstablishmentView, 'establishment')

urlpatterns = [
    path('api/', include(router.urls))
]