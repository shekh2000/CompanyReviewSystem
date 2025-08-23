from rest_framework import serializers
from CompanyReviewSystem.UserManagement.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('created_at', 'last_updated')
        read_only_fields = ('created_at', 'last_updated')
