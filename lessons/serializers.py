from .models import *
from .services import *

from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def validate_video_link(self, value):
        if not is_link_valid(value):
            return serializers.ValidationError('Not valid link')
        return value
