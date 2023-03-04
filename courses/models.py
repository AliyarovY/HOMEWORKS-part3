from django.db import models
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='courses/previews', null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
