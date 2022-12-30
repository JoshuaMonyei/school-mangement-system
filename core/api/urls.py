from django.urls import include, path

urlpatterns = [
    path("auth/", include(("core.authentication.urls", "authentication"))),
    path("users/", include(("core.users.urls", "users"))),
    path("errors/", include(("core.errors.urls", "errors"))),
    path("files/", include(("core.files.urls", "files"))),
]
