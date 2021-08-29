from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Like


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['content', 'posted_date', 'user']


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ['like_date', 'user', 'post']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class AnalyticSerializer(serializers.Serializer):
    date = serializers.DateField(read_only=True)
    count = serializers.IntegerField(read_only=True)
