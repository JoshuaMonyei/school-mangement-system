from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.views import APIView
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

    def post(self, request, format=None):
        # get user id from the request
        auth0_user_id = self.request.data["auth0_user_id"]

        user = User.objects.filter(auth0_user_id=auth0_user_id).first()
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UpdateProfilePicture(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    csrf_exempt = True

    def put(self, request, format=None):
        user_id = self.request.data["user_id"]
        profile_pic = request.FILES.get("file")
        user = User.objects.filter(id=user_id).first()
        if profile_pic:
            subfolder = f"public/profile_picture/{user.id}/"
            filename = default_storage.save(subfolder + profile_pic.name, ContentFile(profile_pic.read()))
            user.profile_pic = settings.BASE_URL + default_storage.url(filename)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
