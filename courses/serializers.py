from .models import *
from rest_framework import serializers


class CouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
