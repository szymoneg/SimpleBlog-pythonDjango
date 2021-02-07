from django.db import models


class Post(models.Model):
    post_owner = models.CharField(max_length=30)
    post_content = models.CharField(max_length=1000)
