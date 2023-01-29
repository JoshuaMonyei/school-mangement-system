from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.common.models import BaseModel
from core.users.models import BaseUser


# class CustomUserManager(BUM):
#     def create_user(self, email, is_active=True, is_admin=False, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)

#         if password is not None:
#             user.set_password(password)
#         else:
#             user.set_unusable_password()

#         user.full_clean()
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email=email,
#             is_active=True,
#             is_admin=True,
#             password=password,
#         )

#         user.is_superuser = True
#         user.save(using=self._db)

#         return user


# class CustomUser(BaseModel, AbstractBaseUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4().hex, editable=False)
#     email = models.EmailField(
#         verbose_name="email address",
#         max_length=255,
#         unique=True,
#     )

#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     # This should potentially be an encrypted field
#     jwt_key = models.UUIDField(default=uuid.uuid4)
#     user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
#     user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"

#     def __str__(self):
#         return self.email

#     def is_staff(self):
#         return self.is_admin


class Department(BaseModel, models.Model):
    department_name = models.CharField(max_length=255)
    objects = models.Manager()


class User(BaseModel, models.Model):
    # admin = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    auth0_user_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name="department")
    profile_pic = models.CharField(max_length=300)
    address = models.TextField()
    session_start_year = models.DateField(auto_now=True)
    session_end_year = models.DateField(null=True, blank=True)
    user_type_data = ((3, "HOD"), (2, "staff"), (1, "student"))
    role = models.IntegerField(default=1, choices=user_type_data)
    objects = models.Manager()


class AdminHOD(BaseModel, models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = models.Manager()


class Staff(BaseModel, models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    objects = models.Manager()


class Subject(BaseModel, models.Model):
    subject_name = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name


class Student(BaseModel, models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
    address = models.TextField()
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()


class CourseRegistration(BaseModel, models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    session_start_year = models.IntegerField()
    session_end_year = models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Subject, related_name="courses")
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
