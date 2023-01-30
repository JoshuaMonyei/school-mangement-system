from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from school_management.models import User, Staff, Department, Subject, Student
from school_management.api.serializers import UserSerializer
from core.users.models import BaseUser


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
        # get user id from the request
        user_id = self.request.data["id"]
        auth0_user_id = self.request.data["auth0_user_id"]

        user_queryset = User.objects.filter(auth0_user_id=auth0_user_id)

        if user_queryset.exists():
            raise ValidationError("User already exists")

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class UpdateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()

    def perform_update(self, serializer):
        # get user id from the request
        user_id = self.request.data["id"]
        auth0_user_id = self.request.data["auth0_user_id"]

        user_queryset = User.objects.filter(auth0_user_id=auth0_user_id)

        if user_queryset.exists():
            raise ValidationError("User already exists")

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
