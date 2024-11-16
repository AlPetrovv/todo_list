from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def __repr__(self):
        return f'{self.id}:{self.email}'