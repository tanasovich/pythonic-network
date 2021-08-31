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
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['last_request']
