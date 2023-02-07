import json
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CourseRegistration, Subject, User, Department
from school_management.api.serializers import (
    UserSerializer,
    DepartmentSerializer,
    SubjectSerializer,
    CourseRegistrationSerializer,
)


class ListDepartment(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class SubjectDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, department_id):
        subjects = Subject.objects.filter(department_id=department_id)
        serializer = SubjectSerializer(subjects, many=True, context={"request": request})
        return Response({"status": "success", "subjects": serializer.data})


class CourseRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        student_id = data.get("student_id")
        session_start_year = data.get("session_start_year")
        session_end_year = data.get("session_end_year")
        department_id = data.get("department_id")
        subject_ids = data.get("subject_ids", [])

        user = User.objects.get(pk=student_id)
        department = Department.objects.get(pk=department_id)
        courses = Subject.objects.filter(pk__in=subject_ids)

        if CourseRegistration.objects.filter(
            student_id=user, session_start_year=session_start_year, session_end_year=session_end_year
        ).exists():
            return Response({"status": "error", "message": "Course registration already exists for this session"})

        course_registration = CourseRegistration.objects.create(
            student_id=user,
            session_start_year=session_start_year,
            session_end_year=session_end_year,
            department_id=department,
        )
        course_registration.courses.set(courses)
        course_registration.save()

        return Response({"status": "success"})
