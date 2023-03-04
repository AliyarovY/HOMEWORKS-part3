import os

from celery import shared_task
from django.core.mail import send_mail

from users.models import User
from payments.models import Payment


@shared_task
def send_notifications(users: list[User], message: str, title: str) -> None:
    send_mail(
        title,
        message,
        os.getenv('EMAIL'),
        users,
        fail_silently=False,
    )


def check_payment_status():
    payment = Payment.objects.last()
    if payment:
        return payment.is_success
    return None