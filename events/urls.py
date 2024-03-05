# in the projectname/appname/urls.py file
from django.urls import path, include
from rest_framework import routers
from events import views

# helps manage urls
router = routers.DefaultRouter()
# this is for registering the Table to REST fw ( row, viewfunc, name)
router.register(r'events', views.EventView , 'event') # r'' => row

# this has API versioning
urlpatterns = [
    # uses rest router func views
    path('api/', include(router.urls))
]