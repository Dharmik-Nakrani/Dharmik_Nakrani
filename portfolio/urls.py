from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_list, name='projects'),
    path('services/', views.services_list, name='services'),
    path('contact/', views.contact, name='contact'),
    path('contact-form/', views.contact_form, name='contact_form'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('download-resume/', views.download_resume, name='download_resume'),
]