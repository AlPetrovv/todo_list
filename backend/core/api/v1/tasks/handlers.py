import logging
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.base.mixins import SerializerByActionMixin
from api.base.permissions import IsOwnerOrAdmin
from api.v1.tasks.serializers import TaskSerializer, CreateTaskSerializer
from api.v1.tasks.serializers import UpdateTaskSerializer
from apps.tasks.models import Task

logger = logging.getLogger('tasks')

class TasksViewSet(
    SerializerByActionMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    serializer_class_by_action = {
        'partial_update': UpdateTaskSerializer,
        'create': CreateTaskSerializer,
    }
    permission_classes = [IsOwnerOrAdmin, ]
    http_method_names = ['get', 'post', 'patch', 'delete']
