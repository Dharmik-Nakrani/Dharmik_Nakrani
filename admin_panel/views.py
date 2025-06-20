from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from portfolio.models import (
    Profile, About, Stats, SkillCategory, Skill, Education,
    Experience, ExperienceResponsibility, Resume
)
from .forms import (
    ProfileForm, AboutForm, StatsForm, SkillCategoryForm, SkillForm,
    EducationForm, ExperienceForm, ExperienceResponsibilityForm, ResumeForm
)

def is_staff_user(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_staff_user)
def dashboard(request):
    """Admin dashboard with overview statistics"""
    context = {
        'total_skills': Skill.objects.count(),
        'total_categories': SkillCategory.objects.count(),
        'total_experiences': Experience.objects.count(),
        'total_education': Education.objects.count(),
        'profile_exists': Profile.objects.exists(),
        'about_exists': About.objects.exists(),
        'stats_exists': Stats.objects.exists(),
        'resume_exists': Resume.objects.exists(),
    }
    return render(request, 'admin_panel/dashboard.html', context)

@login_required
@user_passes_test(is_staff_user)
def profile_management(request):
    """Manage profile information"""
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('admin_panel:profile_management')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'admin_panel/profile_management.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def about_management(request):
    """Manage about section"""
    about = About.objects.first()
    
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'About section updated successfully!')
            return redirect('admin_panel:about_management')
    else:
        form = AboutForm(instance=about)
    
    return render(request, 'admin_panel/about_management.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def stats_management(request):
    """Manage statistics"""
    stats = Stats.objects.first()
    
    if request.method == 'POST':
        form = StatsForm(request.POST, instance=stats)
        if form.is_valid():
            form.save()
            messages.success(request, 'Statistics updated successfully!')
            return redirect('admin_panel:stats_management')
    else:
        form = StatsForm(instance=stats)
    
    return render(request, 'admin_panel/stats_management.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def skills_management(request):
    """Manage skills and categories"""
    categories = SkillCategory.objects.prefetch_related('skills').all()
    
    if request.method == 'POST':
        if 'add_category' in request.POST:
            form = SkillCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Skill category added successfully!')
                return redirect('admin_panel:skills_management')
        elif 'add_skill' in request.POST:
            form = SkillForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Skill added successfully!')
                return redirect('admin_panel:skills_management')
    
    category_form = SkillCategoryForm()
    skill_form = SkillForm()
    
    context = {
        'categories': categories,
        'category_form': category_form,
        'skill_form': skill_form,
    }
    return render(request, 'admin_panel/skills_management.html', context)

@login_required
@user_passes_test(is_staff_user)
def education_management(request):
    """Manage education entries"""
    education_list = Education.objects.all()
    
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education entry added successfully!')
            return redirect('admin_panel:education_management')
    else:
        form = EducationForm()
    
    context = {
        'education_list': education_list,
        'form': form,
    }
    return render(request, 'admin_panel/education_management.html', context)

@login_required
@user_passes_test(is_staff_user)
def experience_management(request):
    """Manage work experience"""
    experiences = Experience.objects.prefetch_related('responsibilities').all()
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience added successfully!')
            return redirect('admin_panel:experience_management')
    else:
        form = ExperienceForm()
    
    context = {
        'experiences': experiences,
        'form': form,
    }
    return render(request, 'admin_panel/experience_management.html', context)

@login_required
@user_passes_test(is_staff_user)
def resume_management(request):
    """Manage resume summary"""
    resume = Resume.objects.first()
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume updated successfully!')
            return redirect('admin_panel:resume_management')
    else:
        form = ResumeForm(instance=resume)
    
    return render(request, 'admin_panel/resume_management.html', {'form': form})

# AJAX Views for dynamic operations
@login_required
@user_passes_test(is_staff_user)
@require_http_methods(["DELETE"])
def delete_skill(request, skill_id):
    """Delete a skill via AJAX"""
    skill = get_object_or_404(Skill, id=skill_id)
    skill.delete()
    return JsonResponse({'success': True, 'message': 'Skill deleted successfully!'})

@login_required
@user_passes_test(is_staff_user)
@require_http_methods(["DELETE"])
def delete_category(request, category_id):
    """Delete a skill category via AJAX"""
    category = get_object_or_404(SkillCategory, id=category_id)
    category.delete()
    return JsonResponse({'success': True, 'message': 'Category deleted successfully!'})

@login_required
@user_passes_test(is_staff_user)
@require_http_methods(["DELETE"])
def delete_education(request, education_id):
    """Delete an education entry via AJAX"""
    education = get_object_or_404(Education, id=education_id)
    education.delete()
    return JsonResponse({'success': True, 'message': 'Education entry deleted successfully!'})

@login_required
@user_passes_test(is_staff_user)
@require_http_methods(["DELETE"])
def delete_experience(request, experience_id):
    """Delete an experience entry via AJAX"""
    experience = get_object_or_404(Experience, id=experience_id)
    experience.delete()
    return JsonResponse({'success': True, 'message': 'Experience deleted successfully!'})

@login_required
@user_passes_test(is_staff_user)
def add_responsibility(request, experience_id):
    """Add responsibility to an experience"""
    experience = get_object_or_404(Experience, id=experience_id)
    
    if request.method == 'POST':
        form = ExperienceResponsibilityForm(request.POST)
        if form.is_valid():
            responsibility = form.save(commit=False)
            responsibility.experience = experience
            responsibility.save()
            messages.success(request, 'Responsibility added successfully!')
        else:
            messages.error(request, 'Error adding responsibility.')
    
    return redirect('admin_panel:experience_management')
