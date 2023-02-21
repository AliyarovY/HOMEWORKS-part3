from django.db import models
from courses.models import Course
from users.models import User


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    preview = models.ImageField(upload_to='lessons/previews', null=True)
    video_link = models.URLField(max_length=255, null=True)
    course = models.ManyToManyField(Course, related_name='lessons', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
