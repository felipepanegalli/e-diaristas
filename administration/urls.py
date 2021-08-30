from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.base import reverse_lazy
from .views.service_views import *
from .views.user_views import *

urlpatterns = [
    # Services
    path("services/", list_service, name="list_service"),
    path("services/create", create_service, name="create_service"),
    path("services/edit/<int:id>", edit_service, name="edit_service"),
    # Users
    path("users/", list_user, name="list_user"),
    path("users/create", create_user, name="create_user"),
    path("users/edit/<int:id>", edit_user, name="edit_user"),
    # Authentication
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("list_service")),
        name="change-password",
    ),
]
