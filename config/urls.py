from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.contrib import admin
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Senin API Başlığın",
        default_version='v1',
        description="Açıklama burada",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # admin panel URL'leri
    path('admin/', admin.site.urls),
    # URL'leriniz
    path('api/', include('journals.urls')),
    path('api/user/', include('user.urls')),

    # JWT token URL'leri
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger UI
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]