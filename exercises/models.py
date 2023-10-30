from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255, unique=True)
    primary_muscle = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=100)
    other_names = models.TextField()  # Store a list of other names as text
    image_url = models.URLField()
    video_url = models.URLField()
    instructions = models.TextField()
    equipment = models.CharField(max_length=255)

    def __str__(self):
        return self.name