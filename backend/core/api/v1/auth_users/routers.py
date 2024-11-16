from rest_framework.routers import SimpleRouter

from .handlers import AuthUserViewSet

user_router = SimpleRouter()
user_router.register('users', AuthUserViewSet, basename='users')

