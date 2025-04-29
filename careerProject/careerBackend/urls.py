from django.urls import path
from . import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static
import os

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:page_name>/', views.my_dynamic_page, name='dynamic_page'),
]

# Serve static files (like images) during development
if settings.DEBUG:
    template_images_dir = os.path.join(settings.BASE_DIR, 'careerBackend', 'templates', 'careerBackend', 'images')
    urlpatterns += static('/images/', document_root=template_images_dir)

    css_dir = os.path.join(settings.BASE_DIR, 'careerBackend', 'templates', 'careerBackend', 'CSS')
    urlpatterns += static('/CSS/', document_root=css_dir)
