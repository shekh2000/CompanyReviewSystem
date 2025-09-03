from django.contrib.admin import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from UserManagement.models import User
from UserManagement.serializers import UserSerializer
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


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

    @action(detail=False, methods=['post'], url_path='login')
    def login(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {'Error': 'Invalid Credentials'},
                status.HTTP_400_BAD_REQUEST,
            )

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        return Response({
            'RefreshToken': str(refresh),
            'AccessToken': str(access),
            'User' : self.serializer_class(user).data
        })

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

    def forgetPassword(self, request):
        pass

