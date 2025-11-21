from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import *

def index(request):
    students = Students.objects.select_related('exams').all()
    return render(request, 'index.html', {'students': students})

def edit_student(request, id):
    try:
        student = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return HttpResponseNotFound("<h2>Student not found</h2>")

    if request.method == "POST":
        student.surname = request.POST.get("surname")
        student.name = request.POST.get("name")
        student.midname = request.POST.get("midname")
        student.gender = request.POST.get("gender")
        student.bday = request.POST.get("bday")
        student.group = request.POST.get("group")
        student.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "edit_student.html", {"student": student})


def edit_exams(request, student_id):
    try:
        student = Students.objects.get(id=student_id)
    except Students.DoesNotExist:
        return HttpResponseNotFound("<h2>Student not found</h2>")

    try:
        exams = Exams.objects.get(student=student)
    except Exams.DoesNotExist:
        exams = Exams(student=student)
        exams.save()

    if request.method == "POST":
        exams.grade_first = request.POST.get("grade_first")
        exams.grade_second = request.POST.get("grade_second")
        exams.grade_third = request.POST.get("grade_third")
        exams.grade_fourth = request.POST.get("grade_fourth")
        exams.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "edit_exams.html", {"student": student, "exams": exams})