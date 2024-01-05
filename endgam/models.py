from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Topbg(models.Model):

    img = models.ImageField(upload_to='Topbg')

class Latest_news(models.Model):

    date_posted = models.DateTimeField(auto_now=True)
    news_title = models.CharField(max_length=100)
    news_desc = models.TextField()
    news_img = models.ImageField(upload_to='newsimg')

class Events_details(models.Model):

    event_img = models.ImageField(upload_to='eventimg')
    event_title = models.TextField(max_length=100)

class Trending(models.Model):

    date_posted = models.DateTimeField(auto_now=True)
    trend_headline = models.TextField()
    trend_img = models.ImageField(upload_to='trendimg')