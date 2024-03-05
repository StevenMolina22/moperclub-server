from django.urls import path, include
from rest_framework import routers
from products import views

router = routers.DefaultRouter()
# table registration
router.register(r'products', views.ProductView, 'product')

urlpatterns = [
  path('api/', include(router.urls))
]