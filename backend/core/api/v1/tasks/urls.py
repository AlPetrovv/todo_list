from django.urls import include
from django.urls import path

from .routers import task_router

urlpatterns = [
    path('', include((task_router.urls, 'tasks'), namespace='tasks')),
]
