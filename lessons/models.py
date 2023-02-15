from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(upload_to='lessons/previews', null=True)
    video_link = models.URLField(max_length=255, null=True)
