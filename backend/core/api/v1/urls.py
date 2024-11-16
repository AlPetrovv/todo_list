from .auth_users.urls import urlpatterns as auth_user_urlpatterns
from .tasks.urls import urlpatterns as tasks_urlpatterns
urlpatterns = [
    *auth_user_urlpatterns,
    *tasks_urlpatterns
]
