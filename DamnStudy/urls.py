from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from courses.views import CourseViewSet
from user.views import UserViewSet


course_router = routers.SimpleRouter()
course_router.register('courses', CourseViewSet, basename='courses')

user_router = routers.SimpleRouter()
user_router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(course_router.urls)),
    path('api/v1/lessons/', include('lessons.urls')),
    path('api/v1/', include(user_router.urls)),

]
