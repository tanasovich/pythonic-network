from rest_framework import viewsets
from rest_framework import permissions

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
