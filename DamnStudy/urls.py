from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from courses.views import CourseViewSet
from users.views import UserViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


course_router = routers.SimpleRouter()
course_router.register('courses', CourseViewSet, basename='courses')

user_router = routers.SimpleRouter()
user_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(course_router.urls)),
    path('api/v1/lessons/', include('lessons.urls')),
    path('api/v1/', include(user_router.urls)),
    path('api/v1/sub/', include('subscriptions.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
