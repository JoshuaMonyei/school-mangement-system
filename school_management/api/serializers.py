from rest_framework import serializers
from school_management.models import User, Department, Subject, CourseRegistration


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = User
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        
class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = "__all__"
        depth = 1
