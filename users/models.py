
from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    """Создали класс менеджера"""

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)    #деактивируем пользователя, но не удаляем
    is_staff = models.BooleanField(default=False)    #определяет, кто может войти в административную часть сайта
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager() #класс UserManager должен управлять объектами этого типа.

    USERNAME_FIELD = 'email'  #определяет, какое поле для входа в систему
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email