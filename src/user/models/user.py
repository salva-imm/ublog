from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import Group, Permission, auth
from django.contrib.auth.models import PermissionsMixin

from django.utils.translation import gettext as _


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='username',
        max_length=128,
        unique=True,
    )
    password = models.CharField(
        verbose_name='password',
        max_length=128,
    )
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set",
        related_query_name="user",
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = _('Users')
        default_permissions = ()
        permissions = [
            ('view_user', _('Can view User')),
            ('add_user', _('Can add User')),
            ('change_user', _('Can edit User')),
            ('delete_user', _('Can delete User')),
            ('view_admin', _('Can view Admin')),
            ('add_admin', _('Can add Admin')),
            ('change_admin', _('Can edit Admin')),
            ('delete_admin', _('Can delete Admin')),
        ]

    def get_group_permissions(self, obj=None):
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_group_permissions"):
                permissions.update(backend.get_group_permissions(self, obj))
        return permissions

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_admin:
            return True

        user_permissions = self.get_group_permissions()
        for permission in user_permissions:
            if permission == perm:
                return True
        return False

    @property
    def is_superuser(self):
        return self.is_admin

    def __str__(self):
        return self.username
