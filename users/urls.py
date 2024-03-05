from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'userprofiles', views.UserProfileView , 'userprofile') # r'' => row

urlpatterns = [
    # uses rest router func views
    path('api/', include(router.urls))
]