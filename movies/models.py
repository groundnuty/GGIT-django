from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    short_desciption = models.TextField()
    published_at = models.DateField()