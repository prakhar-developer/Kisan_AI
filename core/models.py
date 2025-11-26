from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, mobile, **extra_fields):
        if not mobile:
            raise ValueError("Mobile number is required")
        user = self.model(mobile=mobile, **extra_fields)
        user.set_unusable_password()  # OTP login only
        user.save()
        return user

    def create_superuser(self, mobile, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(mobile, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
    ('farmer', _('Farmer')),
    ('vendor', _('Vendor')),
    ('zamindar', _('Zamindar')),
    ('labour', _('Labour')),
    ]

    mobile = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.mobile} ({self.role or 'No role'})"
