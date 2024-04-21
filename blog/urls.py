from django.urls import path, include
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
# (r'name' is the name that appears in the urls after api/ )
router.register(r'posts', views.PostView, 'post')
router.register(r'comments', views.CommentView, 'comment')

urlpatterns = [
    path('api/', include(router.urls))
]