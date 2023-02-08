import json
from django.conf import settings
import stripe
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CourseRegistration, Subject, User, Department
from school_management.api.serializers import (
    UserSerializer,
    DepartmentSerializer,
    SubjectSerializer,
    CourseRegistrationSerializer,
)

stripe.api_key = settings.STRIPE_SECRET_KEY


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
            return Response(
                {"status": "error", "message": "Course registration already exists for this session"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        course_registration = CourseRegistration.objects.create(
            student_id=user,
            session_start_year=session_start_year,
            session_end_year=session_end_year,
            department_id=department,
        )
        course_registration.courses.set(courses)
        course_registration.save()

        return Response({"status": "success"})


class CourseRegistrationDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, student_id):
        course_registrations = CourseRegistration.objects.filter(student_id=student_id)
        serializer = CourseRegistrationSerializer(course_registrations, many=True, context={"request": request})
        return Response({"status": "success", "course_registrations": serializer.data})

class TuitionPaymentIntent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            amount = data.get("amount")
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                automatic_payment_methods={
                    "enabled": True,
                },
            )
            return Response({"clientSecret": intent["client_secret"]})
        except Exception as e:
            return Response({"status": "error", "message": str(e)})
