from django.db import models
from users.models import User
from lessons.models import Lesson
from courses.models import Course


PAYMENT_TYPE_CHOICES = [
    ('PC', 'PC'),
    ('AC', 'AC')
]


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField()
    is_cash = models.BooleanField()
    is_success = models.BooleanField()
    paymentType = models.CharField(max_length=2, choices=PAYMENT_TYPE_CHOICES, default='PC')
