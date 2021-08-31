from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from rest_framework.authtoken.models import Token


class Post(models.Model):
    content = models.CharField(max_length=255)
    posted_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.content


class Like(models.Model):
    like_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    objects = models.Manager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_request = models.DateTimeField(default=timezone.now)

    objects = models.Manager()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print(sender)
    print(instance)
    if created:
        Token.objects.create(user=instance)
        print(Token.objects.get(user=instance))
