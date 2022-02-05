from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, CrewViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'crew', CrewViewSet, basename='crew')

urlpatterns = [
    path('', include(router.urls)),
    path('user/profile/', include('user_profile.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
