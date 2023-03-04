import json

from django.core.management import BaseCommand
from datetime import datetime, timedelta

from django_celery_beat.models import IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.create(
            interval=schedule,
            name='Importing contacts',
            task='DamnStudy.tasks.check_payment_status',
            args=json.dumps([]),
            kwargs=json.dumps({}),
            expires=datetime.utcnow() + timedelta(seconds=30)
        )
