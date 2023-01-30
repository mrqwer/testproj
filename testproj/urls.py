from django.contrib import admin
from django.urls import path, include
from users.views import CustomUserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', CustomUserViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(router.urls)),
    path("api/v1/drf-auth/", include('rest_framework.urls')),
    #path('api/v1/userlist/', CustomUserViewSet.as_view({"get": "list"}))

    #path("api-auth/", include("rest_framework.urls")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
