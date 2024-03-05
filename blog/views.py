from rest_framework import viewsets
from .serializer import PostSerializer, CommentSerializer
from .models import Post, Comment

class PostView(viewsets.ModelViewSet):
  serializer_class = PostSerializer
  queryset = Post.objects.all()

class CommentView(viewsets.ModelViewSet):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
