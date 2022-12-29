from django.db import models

# Create your models here.
from django.db import models


class LikeDislike(models.Model):
    like_count = models.PositiveIntegerField()
    dislike_count = models.PositiveIntegerField()
    total_count = models.PositiveIntegerField()
