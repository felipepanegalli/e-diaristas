from django.urls import path
from .views.service_views import *
from .views.user_views import *

urlpatterns = [
    path("services/", list_service, name="list_service"),
    path("services/create", create_service, name="create_service"),
    path("services/edit/<int:id>", edit_service, name="edit_service"),
    path("users/create", create_user, name="create_user"),
]
