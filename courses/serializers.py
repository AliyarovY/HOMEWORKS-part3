from .models import *

from lessons.models import Lesson
from lessons.serializers import LessonSerializer

from rest_framework import serializers


class CouseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, required=False)


    class Meta:
        model = Course
        fields = ('name', 'preview', 'description', 'lessons_count', 'lessons',)


    def get_lessons_count(self, instance):
        return Lesson.objects.filter(course=instance).count()
