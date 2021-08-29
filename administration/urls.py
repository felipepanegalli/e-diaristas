from django.urls import path
from .views import *

urlpatterns = [
    path("services/", list_service, name="list_service"),
    path("services/create", create_service, name="create_service"),
    path("services/edit/<int:id>", edit_service, name="edit_service"),
]
