from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from listings.views import UserViewSet, PropertyViewSet, ImageViewSet, FavoriteViewSet, InquiryViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'images', ImageViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'inquiries', InquiryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate Listing API",
        default_version='v1',
        description="API docs for the Real Estate Listing platform",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
