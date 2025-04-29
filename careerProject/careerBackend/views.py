from django.shortcuts import render
from django.http import Http404
from django.template.loader import get_template, TemplateDoesNotExist
from django.urls import path

# Create your views here.
def home(request):
    return render(request, 'careerBackend/index.html')

def my_dynamic_page(request, page_name):
    """
    View that tries to render a template with the given page_name.
    """
    try:
        template = get_template(f'careerBackend/{page_name}')  # Construct template name
    except TemplateDoesNotExist:
        raise Http404(f"Page '{page_name}' does not exist")
    return render(request, f'careerBackend/{page_name}')
