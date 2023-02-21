from django.urls import path
from .views import *


urlpatterns = [
    path('delete/<int:pk>/', DeleteLesson.as_view()),
    path('list/', ListLesson.as_view()),
    path('update/<int:pk>/', UpdateLesson.as_view()),
    path('create/', CreateLesson.as_view()),
    path('retrieve/<int:pk>/', RetrieveLesson.as_view()),
]
