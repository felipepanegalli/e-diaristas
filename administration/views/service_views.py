from django.shortcuts import redirect, render
from ..forms.service_forms import ServiceForm
from ..models import Service


def create_service(request):
    if request.method == "POST":
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            service_form.save()
            return redirect("list_service")
    else:
        service_form = ServiceForm()
    return render(request, "services/form.html", {"service_form": service_form})


def list_service(request):
    services = Service.objects.all()
    return render(request, "services/index.html", {"services": services})


def edit_service(request, id):
    service = Service.objects.get(id=id)
    service_form = ServiceForm(request.POST or None, instance=service)
    if service_form.is_valid():
        service_form.save()
        return redirect("list_service")
    return render(request, "services/form.html", {"service_form": service_form})
