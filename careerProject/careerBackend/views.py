from django.shortcuts import render
from django.http import Http404
from django.template.loader import get_template, TemplateDoesNotExist
from django.urls import path

def home(request):
    return render(request, 'careerBackend/index.html')

def about(request):
    return render(request, 'careerBackend/Aboutus.html')

def courses(request):
    return render(request, 'careerBackend/Courses.html')

def defence(request):
    return render(request, 'careerBackend/Defence.html')

def engineering(request):
    return render(request, 'careerBackend/Engineering.html')

def law(request):
    return render(request, 'careerBackend/Law.html')

def medical(request):
    return render(request, 'careerBackend/Medical.html')

def register(request):
    return render(request, 'careerBackend/Register.html')

def contact(request):
    return render(request, 'careerBackend/contactus.html')

def government(request):
    return render(request, 'careerBackend/government.html')

def others(request):
    return render(request, 'careerBackend/others.html')
