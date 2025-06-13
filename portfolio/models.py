from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    name = models.CharField(max_length=100)
    typed_items = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    freelance_status = models.CharField(max_length=50, default='Available')
    address = models.TextField()
    twitter_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    teams_url = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    detailed_description = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

class Stats(models.Model):
    happy_clients = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    support_hours = models.IntegerField(default=0)
    team_members = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Stats - {self.projects} Projects"

    class Meta:
        verbose_name = "Stats"
        verbose_name_plural = "Stats"

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
        ordering = ['order', 'name']

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/', blank=True)
    percentage = models.IntegerField(default=0, help_text="Skill level percentage (0-100)")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}"

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['order', 'name']

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['-start_year', 'order']

class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['-start_date', 'order']

class ExperienceResponsibility(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='responsibilities')
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.experience.position} - Responsibility"

    class Meta:
        ordering = ['order']

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated technologies")
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='services/', blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order', 'title']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

class Resume(models.Model):
    summary = models.TextField()
    pdf_file = models.FileField(upload_to='resume/', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Resume Summary"

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"
