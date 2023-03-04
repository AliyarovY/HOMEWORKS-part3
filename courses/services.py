import os

from django.core.mail import send_mail

from .models import Course
from users.models import User
from subscriptions.models import Subscription


def get_sub_users_from_curse(course: Course) -> list[User]:
    subs = Subscription.objects.filter(course=course)
    result = [sub.user for sub in subs]
    return result



