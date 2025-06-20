from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile_management, name='profile_management'),
    path('about/', views.about_management, name='about_management'),
    path('stats/', views.stats_management, name='stats_management'),
    path('skills/', views.skills_management, name='skills_management'),
    path('education/', views.education_management, name='education_management'),
    path('experience/', views.experience_management, name='experience_management'),
    path('resume/', views.resume_management, name='resume_management'),
    
    # AJAX endpoints
    path('ajax/delete-skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('ajax/delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('ajax/delete-education/<int:education_id>/', views.delete_education, name='delete_education'),
    path('ajax/delete-experience/<int:experience_id>/', views.delete_experience, name='delete_experience'),
    path('ajax/add-responsibility/<int:experience_id>/', views.add_responsibility, name='add_responsibility'),
]