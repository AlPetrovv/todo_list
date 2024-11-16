from django.urls import include
from django.urls import path

from .routers import user_router

urlpatterns = [
    path('', include((user_router.urls, 'auth_users'), namespace='auth_users')),
]
