from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    name = models.CharField(verbose_name="Full Name", max_length=55)
    email = models.EmailField(verbose_name="Email Address", unique=True, max_length=255)
    phone = models.CharField(verbose_name='Phone Number', unique=True, max_length=11)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return self.phone
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin