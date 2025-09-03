from rest_framework import serializers
from UserManagement.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('created_at', 'last_updated')
        read_only_fields = ('created_at', 'last_updated')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        pass
