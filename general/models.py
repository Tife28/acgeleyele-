from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    category = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    sermon_by = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.title

class media(models.Model):
    image = models.ImageField