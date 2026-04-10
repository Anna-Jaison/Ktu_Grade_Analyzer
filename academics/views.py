from django.shortcuts import render
from .models import *
from .utils import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, "home.html", {
        "departments": Department.objects.all(),
        "schemes": Scheme.objects.all()
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

def subjects_view(request):
    if request.method == "POST":
        dept = Department.objects.get(id=request.POST.get("department"))
        scheme = Scheme.objects.get(id=request.POST.get("scheme"))
        semester = Semester.objects.get(
            number=request.POST.get("semester"),
            scheme=scheme
        )

        # ✅ normal subjects + electives (all compulsory)
        subjects = list(Subject.objects.filter(
            department=dept,
            semester=semester
        ))

        return render(request, "subjects.html", {
            "subjects": subjects,
            "semester": semester.id,
            "department": dept.id,
            "dept_name": dept.name
        })

    return HttpResponse("Invalid request")
def result_view(request):
    if request.method == "POST":
        semester_id = request.POST.get("semester")
        department_id = request.POST.get("department")

        # ✅ fetch semester and department objects
        semester = Semester.objects.get(id=semester_id)
        department = Department.objects.get(id=department_id)

        # ✅ subjects for this department and semester only
        subjects = list(Subject.objects.filter(
            department=department,
            semester=semester
        ))

        subjects_data = []
        total_credits = 0

        for sub in subjects:
            internal = float(request.POST.get(f"internal_{sub.id}", 0) or 0)
            
            sub_data = {
                "code": sub.code,
                "name": sub.name,
                "credits": sub.credits,
                "is_lab": sub.is_lab,
                "internal": internal,
                "pass_required": required_external_for_total(
                    internal, PASS_MARK_TOTAL, sub.is_lab
                ),
                "grade_requirements": get_required_externals_by_grade(
                    internal, sub.is_lab
                )
            }
            
            subjects_data.append(sub_data)
            total_credits += sub.credits

        return render(request, "result.html", {
            "subjects": subjects_data,
            "department": department.name,
            "semester": semester.number
        })

    return HttpResponse("Invalid request")