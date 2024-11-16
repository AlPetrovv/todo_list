from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

from api.base.urls import urlpatterns as schemas_urlpatterns
from api.v1.urls import urlpatterns as v1_urlpatterns

patterns = [
    path('admin/', admin.site.urls),
]

if settings.I18N_URLS_ENABLED:
    urlpatterns = i18n_patterns(*patterns)
else:
    urlpatterns = patterns

urlpatterns += [
    path('api/v1/', include(v1_urlpatterns)),
    *schemas_urlpatterns,
    re_path(r'^api/auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'TodoList admin'
admin.site.site_title = 'TodoList admin'
admin.site.index_title = 'TodoList'
