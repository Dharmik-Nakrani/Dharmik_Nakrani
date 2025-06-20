from django import forms
from portfolio.models import (
    Profile, About, Stats, SkillCategory, Skill, Education,
    Experience, ExperienceResponsibility, Resume
)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'typed_items': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'freelance_status': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'teams_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = '__all__'
        widgets = {
            'happy_clients': forms.NumberInput(attrs={'class': 'form-control'}),
            'projects': forms.NumberInput(attrs={'class': 'form-control'}),
            'support_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'team_members': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['name', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Display Order'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'name', 'percentage', 'order']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skill Name'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Display Order'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'start_year': forms.TextInput(attrs={'class': 'form-control'}),
            'end_year': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ExperienceResponsibilityForm(forms.ModelForm):
    class Meta:
        model = ExperienceResponsibility
        fields = ['description', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }