from django.db import models
import datetime
from django.db.models.fields import CharField, URLField

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
    url = URLField(blank=True)