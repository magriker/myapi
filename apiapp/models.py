from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64)


class Article(models.Model):
    user = models.ForeignKey(User,related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    contents = models.TextField()