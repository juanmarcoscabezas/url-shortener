from django.db import models
import uuid

# Create your models here.

class ShortenerModel(models.Model):
    source_url = models.URLField(unique=True)
    encoded = models.CharField(max_length=40, unique=True, default='')
    title = models.CharField(max_length=100, default='')
    views = models.PositiveBigIntegerField(default=0)
