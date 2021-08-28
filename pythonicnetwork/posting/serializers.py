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
