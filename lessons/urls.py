from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<int:pk>/', DetailLesson.as_view()),
    path('list/', ListLesson.as_view())
]
