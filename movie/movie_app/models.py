from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField()
    director=models.CharField()
    year=models.IntegerField()
    language=models.CharField()
    image=models.ImageField(upload_to='images')
    description=models.TextField()
