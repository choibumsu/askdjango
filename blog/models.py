from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100,
    choices = (
        ('제목1', '제목1 레이블'),
        ('제목2', '제목2 레이블'),
        ('제목3', '제목3 레이블'),
    ))
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
