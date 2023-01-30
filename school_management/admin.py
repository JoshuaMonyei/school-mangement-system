from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from school_management.models import User, Department, Subject, Student, Staff, CourseRegistration

# class UserModel(UserAdmin):
#     pass


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(CourseRegistration)