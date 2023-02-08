from django.urls import include, path
from django.contrib import admin
import school_management.views as views
import school_management.hod_views as HodViews
import school_management.staff_views as StaffViews
import school_management.student_views as StudentViews


urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup", views.UserCreate.as_view(), name="signup"),
    path("get-user/<str:pk>", views.UserDetail.as_view(), name="get-user"),
    path("update-profile", views.UpdateUser.as_view(), name="update-user"),
    path("update-profile-picture", views.UpdateProfilePicture.as_view(), name="update-profile-picture"),
    path("get-departments", StudentViews.ListDepartment.as_view(), name="get-departments"),
    path("get-department/<str:pk>", StudentViews.DepartmentDetail.as_view(), name="get-department"),
    path("get-subjects/<str:department_id>", StudentViews.SubjectDetail.as_view(), name="get-subjects"),
    path("register-course", StudentViews.CourseRegistrationView.as_view(), name="register-course"),
    path("create-payment-intent", StudentViews.TuitionPaymentIntent.as_view(), name="create-payment-intent"),
    #     Staff URL Path
    path("staff_home", StaffViews.staff_home, name="staff_home"),
]
