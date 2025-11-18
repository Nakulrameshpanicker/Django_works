from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=40)
    price=models.IntegerField(max_length=40)
    pages=models.IntegerField(max_length=20)
    language=models.CharField(max_length=40)
    image=models.ImageField(upload_to='images')