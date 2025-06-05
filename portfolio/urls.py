from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('send-message/', views.contact_form, name='contact_form'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
]