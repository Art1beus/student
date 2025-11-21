from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import *

def index(request):
    students = Students.objects.all()
    exams = Exams.objects.all()
    return render(request, 'index.html', {'students':students, 'exams':exams})

def edit(request, id):
    try:
        student = Students.objects.get(id=id)
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
            return render(request, "edit.html", {"student": student})
    except Students.DoesNotExist:
        return HttpResponseNotFound("<h2>Student not found</h2>")
    
def delete(request, id):
    try:
        student = Students.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect("/")
    except Students.DoesNotExist:
        return HttpResponseNotFound("<h2>Student not found</h2>")

def create(request):
    if request.method == "POST":
        student = Students()
        student.surname = request.POST.get("surname")
        student.name = request.POST.get("name")
        student.midname = request.POST.get("midname")
        student.gender = request.POST.get("gender")
        student.bday = request.POST.get("bday")
        student.group = request.POST.get("group")
        student.save()
        return HttpResponseRedirect("/")
    students = Students.objects.all()
    return render(request, "create.html", {"students": students})