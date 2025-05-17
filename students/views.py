from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student

def index(request):
    students = Student.objects.all()
    return HttpResponse(students)

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return HttpResponse(student)
