from django.contrib.admin import ModelAdmin
from django.contrib.admin import register

from .models import AuthUser


@register(AuthUser)
class UserAuthAdmin(ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'is_admin')
