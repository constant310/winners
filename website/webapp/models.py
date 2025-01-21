from django.db import models
from ckeditor.fields import RichTextField

class Event(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField()
  
    def __str__(self):
        return self.title
class Testimony(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    testimony_date = models.DateField()

    def __str__(self):
        return self.title
class Latest_news(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    news_date = models.DateField()

    def __str__(self):
        return self.title
class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo_date = models.DateField()

    def __str__(self):
        return self.title