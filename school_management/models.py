from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from core.common.models import BaseModel
from core.users.models import BaseUser


class Department(BaseModel, models.Model):
    department_name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.department_name


class User(BaseModel, models.Model):
    auth0_user_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name="department")
    profile_pic = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(max_length=255)
    campus = models.CharField(max_length=255)
    session_start_year = models.DateField(auto_now=True)
    session_end_year = models.DateField(null=True, blank=True)
    user_type_data = ((3, "HOD"), (2, "staff"), (1, "student"))
    role = models.IntegerField(choices=user_type_data)
    objects = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Subject(BaseModel, models.Model):
    subject_name = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    class_grade_type = (
        ("freshman", "freshman"),
        ("sophomore", "sophomore"),
        ("junior", "junior"),
        ("senior", "senior"),
    )
    class_grade = models.CharField(max_length=255, default="freshman", choices=class_grade_type)
    course_data_type = (
        ("core", "core"),
        ("elective", "elective"),
    )
    course_type = models.CharField(max_length=255, default="core", choices=course_data_type)
    credit_unit = models.IntegerField(default=2)
    course_code = models.CharField(max_length=255)
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name


class CourseRegistration(BaseModel, models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    session_start_year = models.IntegerField()
    session_end_year = models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Subject, related_name="courses")
    objects = models.Manager()


class AdminHOD(BaseModel, models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = models.Manager()


class Staff(BaseModel, models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    objects = models.Manager()


class Student(BaseModel, models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
    address = models.TextField()
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()


class Attendance(BaseModel, models.Model):
    subject_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AttendanceReport(BaseModel, models.Model):
    student_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    objects = models.Manager()


class LeaveReportStudent(BaseModel, models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    objects = models.Manager()


class LeaveReportStaff(BaseModel, models.Model):
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    objects = models.Manager()


class FeedBackStudent(BaseModel, models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    objects = models.Manager()


class FeedBackStaff(BaseModel, models.Model):
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    objects = models.Manager()


class NotificationStudent(BaseModel, models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    objects = models.Manager()


class NotificationStaff(BaseModel, models.Model):
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    objects = models.Manager()
