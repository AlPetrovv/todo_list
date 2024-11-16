from rest_framework.viewsets import ModelViewSet

from .mixins import SerializerByActionMixin


class BaseViewSet(SerializerByActionMixin, ModelViewSet):
    ...

