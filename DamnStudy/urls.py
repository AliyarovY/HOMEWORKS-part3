from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from courses.views import CourseViewSet
from users.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# yasg----------------------------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# routers ------------------------------------------------
course_router = routers.SimpleRouter()
course_router.register('courses', CourseViewSet, basename='courses')

user_router = routers.SimpleRouter()
user_router.register('users', UserViewSet, basename='users')
# ----------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(course_router.urls)),
    path('api/lessons/', include('lessons.urls')),
    path('api/', include(user_router.urls)),
    path('api/', include('subscriptions.urls')),
    path('api/payments', include('payments.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
