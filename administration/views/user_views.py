from ..forms.user_forms import UserForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model


def create_user(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("list_user")
    else:
        user_form = UserForm()
    return render(request, "users/form.html", {"user_form": user_form})


def list_user(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=True)
    return render(request, "users/index.html", {"users": users})
