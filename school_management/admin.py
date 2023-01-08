from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from core.users.models import BaseUser


# class UserModel(UserAdmin):
#     pass


# admin.site.register(BaseUser, UserModel)
