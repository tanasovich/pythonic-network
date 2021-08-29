from django.db.models.functions import TruncDay
from django.db.models import Count
from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnalyticsView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request: Request, format=None):
        date_from = request.query_params['date_from']
        date_to = request.query_params['date_to']
        queryset = Like.objects\
            .annotate(date=TruncDay('like_date'))\
            .values('date')\
            .annotate(count=Count('id'))\
            .values('date', 'count')

        return Response(JSONRenderer().render(queryset))
