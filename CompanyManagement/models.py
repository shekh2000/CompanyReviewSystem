from django.db import models
from django.conf import settings

class Company(models.Model):
    class CategoryType(models.TextChoices):
        IT = "IT", "Information Technology"
        FINANCE = "Finance", "Finance"
        HEALTHCARE = "Healthcare", "Healthcare"

    company_name = models.CharField(max_length=50, unique=True)
    category = models.CharField(
        max_length=50,
        choices=CategoryType.choices
    )
    description = models.TextField(blank=False)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="companies"
    )
    country = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} ({self.category})"
