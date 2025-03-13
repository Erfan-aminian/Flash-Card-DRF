from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import CreateUserProfileSerializer
#Create your views here.
class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateUserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_data = User(
            username=data['username'],
            email=data['email'],
        )
        user_data.set_password(data['password'])
        user_data.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

