from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#a-full-example



class UserManager(BaseUserManager):

    def create_superuser(self, email, name, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self._create_user(email, name, password, **extra_fields)


    def create_user(self, email, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password, **extra_fields)
    

    def _create_user(self, email, name, password, **extra_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        user = self.model(email=email,name=name, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(f"{self.name} - {self.email}")

    def get_name(self):
        return str(self.name)
