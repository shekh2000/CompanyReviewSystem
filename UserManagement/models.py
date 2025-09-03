from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if email is None:
            raise ValueError("Email can not be empty.")
        user = self.normalize_email(email)
        user = self.model(email=user, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    class RoleType(models.TextChoices):
        USER = "User", "User"
        MANAGER = "Manager", "Manager"
        ADMIN = "Admin", "Admin"

    username = None
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    dob = models.DateField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=RoleType.choices,
        default=RoleType.USER
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return self.email
