from django.contrib.admin import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from UserManagement.models import User
from UserManagement.serializers import UserSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self,request):
        pass

    def logout(self, request):
        pass

    def getUser(self, request):
        pass

    def updateUser(self, request):
        pass

    def deleteUser(self, request):
        pass

    def listUsers(self, request):
        pass

    def updatePassword(self, request):
        pass


