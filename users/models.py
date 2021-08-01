from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings
import django.contrib.auth.models
from datetime import datetime, timedelta
import jwt


class UserManager(django.contrib.auth.models.BaseUserManager):
    """Создали класс менеджера"""

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('У пользователей должно быть имя пользователя.')

        if email is None:
            raise TypeError('У пользователей должен быть адрес электронной почты.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, *args, **kwargs):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save()

        return user


class User(django.contrib.auth.models.AbstractBaseUser, django.contrib.auth.models.PermissionsMixin):
    """
    Модель пользователя
    """
    username = models.CharField(db_index=True, max_length=255, unique=True, default='1')
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)  # деактивируем пользователя, но не удаляем
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'  # определяет, какое поле для входа в систему
    REQUIRED_FIELDS = ['username']

    objects = UserManager()  # класс UserManager должен управлять объектами этого типа.

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        return self.staff

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    @property
    def is_admin(self):
        # "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        # "Is the user active?"
        return self.active
