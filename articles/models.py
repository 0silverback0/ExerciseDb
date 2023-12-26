from django.db import models
from django.utils import timezone

# Create your models here.

def get_current_date():
    return timezone.now().date()

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    date = models.DateField(default=get_current_date, editable=False)
    text = models.TextField()
    image = models.TextField(default='https://via.placeholder.com/800x400')
    top_article = models.BooleanField(default=False)
    category = models.TextField(default='general')
    description = models.TextField(100)
