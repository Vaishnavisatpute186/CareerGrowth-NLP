from django.shortcuts import render
from django.http import Http404
from django.template.loader import get_template, TemplateDoesNotExist
from django.urls import path
from django.http import JsonResponse
import random
from .nlp_suggestor import suggest

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

def contact(request):
    return render(request, 'careerBackend/contactus.html')

def government(request):
    return render(request, 'careerBackend/government.html')

def others(request):
    return render(request, 'careerBackend/others.html')

def register(request):
    if request.method == 'POST':
        qualification = request.POST.get('Qualifications')
        skills = request.POST.get('Skills:')
        interests = request.POST.get('Interests:')
        field, job_title = suggest(qualification, skills, interests)
        message = 'Suggested field ' + field
        # url = f"/{choice}/"
        data = {
            'message': message,
            'career': field,
            # 'redirect_url': url,
        }
        return JsonResponse(data)  #  Send back a JSON response
    return render(request, 'careerBackend/Register.html')
