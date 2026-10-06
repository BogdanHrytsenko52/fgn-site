from django.shortcuts import get_object_or_404, render

from .models import Department, Exchange, HomePage, Program


def home(request):
    home_page = HomePage.objects.first()
    return render(request, "faculty/home.html", {"home_page": home_page})


def programs(request):
    programs = Program.objects.select_related("department").all()
    return render(request, "faculty/programs.html", {"programs": programs})


def program_detail(request, id):
    program = get_object_or_404(Program, id=id)
    return render(request, "faculty/program_detail.html", {"program": program})


def departments(request):
    departments = Department.objects.all()
    return render(request, "faculty/departments.html", {"departments": departments})


def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(
        request,
        "faculty/department_detail.html",
        {"department": department},
    )


def exchange(request):
    exchanges = Exchange.objects.all().order_by("deadline")
    return render(request, "faculty/exchange.html", {"exchanges": exchanges})
