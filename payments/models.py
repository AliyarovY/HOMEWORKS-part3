from django.db import models
from users.models import User
from lessons.models import Lesson
from courses.models import Course


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveBigIntegerField()
    is_cash = models.BooleanField()
