from django.db import models
from users.models import User
from courses.models import Course


class Subscription(models.Model):
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

