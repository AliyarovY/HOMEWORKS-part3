from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from base.permissions import IsModerator, IsSelf, IsNotModerator
from base.services import moderator_queryset

from .serializers import *


class ListLesson(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return moderator_queryset(Lesson, self.request.user)
        return Lesson.objects.all()


class RetrieveLesson(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsSelf, IsAuthenticated]


class DeleteLesson(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsSelf, IsAuthenticated, IsNotModerator]


class UpdateLesson(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsSelf, IsAuthenticated]


class CreateLesson(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsNotModerator]
