from django.urls import include, path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
]

# from .apis import (
#     UserJwtLoginApi,
#     UserJwtLogoutApi,
#     UserMeApi,
#     UserSessionLoginApi,
#     UserSessionLogoutApi,
# )

# urlpatterns = [
#     path(
#         "session/",
#         include(
#             (
#                 [
#                     path("login/", UserSessionLoginApi.as_view(), name="login"),
#                     path("logout/", UserSessionLogoutApi.as_view(), name="logout"),
#                 ],
#                 "session",
#             )
#         ),
#     ),
#     path(
#         "jwt/",
#         include(
#             (
#                 [
#                     path("login/", UserJwtLoginApi.as_view(), name="login"),
#                     path("logout/", UserJwtLogoutApi.as_view(), name="logout"),
#                 ],
#                 "jwt",
#             )
#         ),
#     ),
#     path("me/", UserMeApi.as_view(), name="me"),
# ]
