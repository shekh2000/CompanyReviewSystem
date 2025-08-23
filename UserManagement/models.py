from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    class RoleType(models.TextChoices):
        USER = "User", "User"
        MANAGER = "Manager", "Manager"
        ADMIN = "Admin", "Admin"

    username = None
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
