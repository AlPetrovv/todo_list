from drf_spectacular import views

from django.urls import path

urlpatterns = [
    path('api/schema/', views.SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', views.SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', views.SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
