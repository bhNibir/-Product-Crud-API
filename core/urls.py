from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import static
from . import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Themexpert Task API",
      default_version='v1',
      description="""Themexpert Task API.
      The `swagger-ui` view can be found [here](/api/doc).
The `ReDoc` view can be found [here](/api/redoc).
The swagger YAML document can be found [here](/api/doc.yaml).
You can log in using the pre-existing `admin` user with password `password`.""",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
    #apis Docs
    re_path(r'^api/doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)