from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Like, Profile


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['id', 'content', 'posted_date', 'user']
        read_only_fields = ['id']

    def save(self, **kwargs):
        kwargs['user'] = self.fields['user'].get_default()
        return super().save(**kwargs)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ['id', 'like_date', 'user', 'post']
        read_only_fields = ['id']

    def save(self, **kwargs):
        kwargs['user'] = self.fields['user'].get_default()
        return super().save(**kwargs)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['last_request']
