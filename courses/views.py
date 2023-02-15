from .serializers import *
from rest_framework import viewsets
from .models import Course


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CouseSerializer
