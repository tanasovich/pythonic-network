from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    content = models.CharField(max_length=255)
    posted_date = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
