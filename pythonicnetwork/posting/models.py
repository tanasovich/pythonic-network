from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=256)
    likes_count = models.IntegerField()
