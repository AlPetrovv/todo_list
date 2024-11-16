from rest_framework.routers import SimpleRouter

from .handlers import TasksViewSet

task_router = SimpleRouter()
task_router.register('tasks', TasksViewSet, basename='tasks')