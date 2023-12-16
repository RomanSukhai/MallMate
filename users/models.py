from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db import models



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mall(models.Model):
    cities = models.ManyToManyField(City, related_name='malls')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Shop(models.Model):
    mall = models.ForeignKey(Mall, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=100)
    icon_image = models.ImageField(upload_to='shop_icons/')
    x = models.DecimalField(max_digits=9, decimal_places=6)
    y = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.name} in {self.mall.name}"
