from django.contrib import admin
from .models import (
    Profile, About, Stats, SkillCategory, Skill, Education,
    Experience, ExperienceResponsibility, Project, Service,
    ContactMessage, Resume
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'city', 'is_active', 'updated_at']
    list_filter = ['is_active', 'city', 'created_at']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'updated_at']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ['happy_clients', 'projects', 'support_hours', 'team_members', 'is_active']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['created_at', 'updated_at']

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'image', 'percentage', 'order', 'is_active']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order', 'is_active', 'skill_count']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SkillInline]
    def skill_count(self, obj):
        return obj.skills.filter(is_active=True).count()
    skill_count.short_description = 'Active Skills'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'percentage', 'order', 'is_active']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'category__name']
    list_editable = ['percentage', 'order', 'is_active']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'is_active', 'order']
    list_filter = ['is_active', 'start_year', 'institution']
    search_fields = ['degree', 'institution', 'location']
    list_editable = ['order', 'is_active']

class ExperienceResponsibilityInline(admin.TabularInline):
    model = ExperienceResponsibility
    extra = 1
    fields = ['description', 'order']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_active']
    list_filter = ['is_active', 'company', 'start_date']
    search_fields = ['position', 'company', 'location']
    inlines = [ExperienceResponsibilityInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'is_active', 'created_at']
    list_filter = ['is_featured', 'is_active', 'created_at', 'start_date']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_featured', 'is_active']
    date_hierarchy = 'created_at'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'is_active']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    def has_add_permission(self, request):
        return False  # Prevent manual addition through admin

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['summary', 'is_active', 'updated_at']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    # Optionally, you can add custom actions or methods here for ResumeAdmin
    # For example, to download the resume directly from the admin list view:
    def download_link(self, obj):
        if obj.pdf_file:
            return f'<a href="{obj.pdf_file.url}" target="_blank">Download</a>'
        return "-"
    download_link.allow_tags = True
    download_link.short_description = "Download Resume"

    # Add 'download_link' to list_display if you want the download link visible
    # list_display = ['summary', 'is_active', 'updated_at', 'download_link']
