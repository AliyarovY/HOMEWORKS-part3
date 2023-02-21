from rest_framework import generics
from base.permissions import IsModerator, IsSelf
from base.services import moderator_queryset

from .serializers import *


class ListLesson(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        return moderator_queryset(Lesson, self.request.user)


class RetrieveLesson(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsSelf]


class DeleteLesson(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsSelf]


class UpdateLesson(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsSelf]


class CreateLesson(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
