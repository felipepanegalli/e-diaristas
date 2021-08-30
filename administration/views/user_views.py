from ..forms.user_forms import CreateUserForm, EditUserForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model


def create_user(request):
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("list_user")
    else:
        user_form = CreateUserForm()
    return render(request, "users/add.html", {"user_form": user_form})


def list_user(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=True)
    return render(request, "users/index.html", {"users": users})


def edit_user(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    user_form = EditUserForm(request.POST or None, instance=user)
    if user_form.is_valid():
        user_form.save()
        return redirect("list_user")
    return render(request, "users/edit.html", {"user_form": user_form})
