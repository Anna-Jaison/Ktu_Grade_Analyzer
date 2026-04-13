from django.shortcuts import render
from .models import *
from .utils import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from extract_subject import DATA
def home(request):
    departments = [
        {"id": 1, "name": "CSE"},
        {"id": 2, "name": "ECE"},
        {"id": 3, "name": "EEE"},
    ]

    schemes = [
        {"id": 1, "year": 2019},
        {"id": 2, "year": 2024},
    ]

    return render(request, "home.html", {
        "departments": departments,
        "schemes": schemes
    })

@csrf_exempt
def save_elective(request):
    if request.method == "POST":
        data = json.loads(request.body)
        subject_id = data.get("subject_id")
        semester_id = data.get("semester_id")

        if not request.user.is_authenticated:
            return JsonResponse({"message": "Login required"}, status=401)

        subject = Subject.objects.get(id=subject_id)
        semester = Semester.objects.get(id=semester_id)

        obj, created = StudentElective.objects.get_or_create(
            student=request.user,
            semester=semester,
            subject=subject
        )

        if not created:
            obj.delete()
            return JsonResponse({"message": "Removed"})

        return JsonResponse({"message": "Added"})

import json
import os
from django.shortcuts import render

def subjects_view(request):
    subjects = []
    department = None
    semester = None
    scheme = None

    if request.method == "POST":
        department = request.POST.get("department")
        semester = request.POST.get("semester")
        scheme = request.POST.get("scheme")

        if department and semester:
            file_path = os.path.join(os.path.dirname(__file__), "../subjects.json")

            with open(file_path, "r") as f:
                data = json.load(f)

            subjects = [s for s in data if s.get('dept') == department and str(s.get('sem')) == semester and s.get('scheme', 2019) == int(scheme)]

    return render(request, "subjects.html", {
        "subjects": subjects,
        "selected_department": department,
        "selected_semester": semester,
        "selected_scheme": scheme
    })
def result_view(request):
    if request.method == "POST":
        department = request.POST.get("department")
        semester = request.POST.get("semester")
        scheme = int(request.POST.get("scheme"))

        file_path = os.path.join(os.path.dirname(__file__), "../subjects.json")

        with open(file_path, "r") as f:
            data = json.load(f)

        subjects = [
            s for s in data
            if s.get('dept') == department
            and str(s.get('sem')) == semester
            and s.get('scheme', 2019) == scheme
        ]

        subjects_data = []

        for sub in subjects:
            internal = float(request.POST.get(f"internal_{sub['code']}", 0) or 0)

            pass_total = get_pass_mark_total(scheme)

            max_internal = sub.get("max_internal")
            max_external = sub.get("max_external")

            required_value, required_status = required_external_for_total(
    internal,
    pass_total,
    max_external,
    scheme
)

            sub_data = {
                "code": sub["code"],
                "name": sub["name"],
                "credits": sub["credits"],
                "internal": internal,
                "max_internal": max_internal,
                "max_external": max_external,
                "pass_required": required_value,
                "pass_status": required_status,
                "can_pass": required_value != "Not Possible" and required_value <= max_external,
                "ese_min": round(max_external * (0.40 if scheme == 2024 else 0.35), 2),

                "grade_requirements": get_required_externals_by_grade(
                    internal,
                    max_external,
                    scheme
                )
            }

            subjects_data.append(sub_data)

        return render(request, "result.html", {
            "subjects": subjects_data,
            "department": department,
            "semester": semester
        })

    return HttpResponse("Invalid request")