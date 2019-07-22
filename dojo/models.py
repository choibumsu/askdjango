from django.db import models

# Create your models here.
class Post(models.Model):
    author_name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    text = models.TextField()

class Account(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

