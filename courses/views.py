from time import timezone

from DamnStudy.tasks import send_notifications
from .serializers import *
from rest_framework import viewsets
from .models import Course
from .services import get_sub_users_from_curse


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CouseSerializer

    def perform_update(self, serializer):
        course = self.get_object()
        last_update_time = course.updated_time
        sub_users = get_sub_users_from_curse(course)
        message = f'course {course} is updated'
        title = 'course update'
        is_actual = timezone.now() - last_update_time >= timezone.timedelta(hours=4)
        if sub_users and is_actual:
            send_notifications.delay(sub_users, message, title)

        super().perform_update(self, serializer)



