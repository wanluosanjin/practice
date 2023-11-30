from django.db import models

# Create your models here.

class ju(models.Model):
    name = models.CharField(max_length=16)
    ju = models.TextField()
    time = models.TimeField()
