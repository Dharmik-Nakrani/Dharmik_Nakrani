from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse

from .models import (
    Profile, About, Stats, SkillCategory, Skill, Education,
    Experience, ExperienceResponsibility, Project, Service,
    ContactMessage, Resume
)

# --- Utility: Fallback Context with Dummy Data ---
def get_fallback_context():
    return {
        'title': 'Portfolio - Professional Developer',
        'profile': {
            'name': 'John Developer',
            'typed_items': 'Full Stack Developer, DevOps Engineer, Freelancer',
            'website': 'johndeveloper.example.com',
            'phone': '+1 234 567 8900',
            'city': 'New York, USA',
            'email': 'john@example.com',
            'freelance_status': 'Available',
            'address': 'New York, NY, USA',
            'twitter_url': 'https://twitter.com/johndeveloper',
            'facebook_url': 'https://facebook.com/johndeveloper',
            'instagram_url': 'https://instagram.com/johndeveloper',
            'linkedin_url': 'https://linkedin.com/in/johndeveloper',
            'teams_url': 'skype:john.developer',
        },
        'about': {
            'description': 'Passionate software engineer with expertise in modern web technologies, cloud platforms, and automation.',
            'title': 'Full Stack Developer & DevOps Specialist',
            'subtitle': 'Dedicated to creating efficient, scalable, and user-friendly solutions.',
            'detailed_description': 'I specialize in full-stack development, cloud infrastructure, and DevOps practices using cutting-edge technologies. My goal is to deliver high-quality solutions that exceed expectations.',
            'image': 'https://linkedin.com/in/johndeveloper'
        },
        'stats': {
            'happy_clients': 30,
            'projects': 75,
            'support_hours': 1200,
            'team_members': 8,
        },
        'skill_categories': [
            {
                'name': 'Frontend',
                'slug': 'frontend',
                'skills': [
                    {'name': 'React', 'image': 'img/skills/React.png', 'percentage': 90},
                    {'name': 'Vue.js', 'image': 'img/skills/Vue.png', 'percentage': 85},
                    {'name': 'Angular', 'image': 'img/skills/Angular.png', 'percentage': 75},
                    {'name': 'JavaScript', 'image': 'img/skills/JavaScript.png', 'percentage': 95},
                    {'name': 'TypeScript', 'image': 'img/skills/TypeScript.png', 'percentage': 80},
                    {'name': 'HTML5', 'image': 'img/skills/HTML5.png', 'percentage': 95},
                    {'name': 'CSS3', 'image': 'img/skills/CSS3.png', 'percentage': 90},
                ]
            },
            {
                'name': 'Backend',
                'slug': 'backend',
                'skills': [
                    {'name': 'Node.js', 'image': 'img/skills/NodeJS.png', 'percentage': 90},
                    {'name': 'Python', 'image': 'img/skills/Python.png', 'percentage': 85},
                    {'name': 'Django', 'image': 'img/skills/Django.png', 'percentage': 80},
                    {'name': 'Express.js', 'image': 'img/skills/Express.png', 'percentage': 85},
                    {'name': 'PHP', 'image': 'img/skills/PHP.png', 'percentage': 70},
                    {'name': 'Laravel', 'image': 'img/skills/Laravel.png', 'percentage': 75},
                ]
            },
            {
                'name': 'DevOps',
                'slug': 'devops',
                'skills': [
                    {'name': 'Docker', 'image': 'img/skills/Docker.png', 'percentage': 85},
                    {'name': 'Kubernetes', 'image': 'img/skills/Kubernetes.png', 'percentage': 75},
                    {'name': 'AWS', 'image': 'img/skills/AWS.png', 'percentage': 80},
                    {'name': 'Jenkins', 'image': 'img/skills/Jenkins.png', 'percentage': 70},
                    {'name': 'Terraform', 'image': 'img/skills/Terraform.png', 'percentage': 65},
                    {'name': 'Git', 'image': 'img/skills/Git.png', 'percentage': 90},
                ]
            },
            {
                'name': 'Database',
                'slug': 'database',
                'skills': [
                    {'name': 'MySQL', 'image': 'img/skills/MySQL.png', 'percentage': 85},
                    {'name': 'PostgreSQL', 'image': 'img/skills/PostgreSQL.png', 'percentage': 80},
                    {'name': 'MongoDB', 'image': 'img/skills/MongoDB.png', 'percentage': 75},
                    {'name': 'Redis', 'image': 'img/skills/Redis.png', 'percentage': 70},
                    {'name': 'SQLite', 'image': 'img/skills/SQLite.png', 'percentage': 85},
                ]
            },
            {
                'name': 'Mobile',
                'slug': 'mobile',
                'skills': [
                    {'name': 'React Native', 'image': 'img/skills/ReactNative.png', 'percentage': 80},
                    {'name': 'Flutter', 'image': 'img/skills/Flutter.png', 'percentage': 75},
                    {'name': 'Ionic', 'image': 'img/skills/Ionic.png', 'percentage': 70},
                    {'name': 'Swift', 'image': 'img/skills/Swift.png', 'percentage': 60},
                ]
            },
        ],
        'resume': {
            'summary': 'Innovative and results-driven Full Stack Developer with 5+ years of experience designing and implementing scalable web applications and cloud solutions from concept to deployment.',
            'pdf_file': ''
        },
        'educations': [
            {
                'degree': 'Bachelor of Computer Science',
                'start_year': '2016',
                'end_year': '2020',
                'institution': 'Tech University',
                'location': 'California, USA',
                'description': 'Specialized in software engineering and computer systems. Completed projects in web development, mobile applications, and database management.'
            },
            {
                'degree': 'Master of Software Engineering',
                'start_year': '2020',
                'end_year': '2022',
                'institution': 'Advanced Tech Institute',
                'location': 'New York, USA',
                'description': 'Advanced studies in software architecture, cloud computing, and DevOps practices. Thesis on microservices architecture and containerization.'
            }
        ],
        'experiences': [
            {
                'position': 'Senior Full Stack Developer',
                'start_date': '2022',
                'end_date': 'Present',
                'company': 'Tech Solutions Inc.',
                'location': 'New York, USA',
                'responsibilities': [
                    {'description': 'Lead development of scalable web applications using React, Node.js, and cloud technologies'},
                    {'description': 'Implement CI/CD pipelines and DevOps practices to streamline deployment processes'},
                    {'description': 'Mentor junior developers and conduct code reviews to maintain high code quality'},
                    {'description': 'Collaborate with cross-functional teams to deliver projects on time and within budget'},
                ]
            },
            {
                'position': 'Full Stack Developer',
                'start_date': '2020',
                'end_date': '2022',
                'company': 'Digital Innovations LLC',
                'location': 'California, USA',
                'responsibilities': [
                    {'description': 'Developed responsive web applications using modern JavaScript frameworks'},
                    {'description': 'Built RESTful APIs and integrated third-party services'},
                    {'description': 'Optimized database queries and improved application performance'},
                    {'description': 'Participated in agile development processes and sprint planning'},
                ]
            }
        ],
        'contact_info': {
            'address': 'New York, NY, USA',
            'phone': '+1 234 567 8900',
            'email': 'john@example.com',
        },
        'projects': [],
        'services': [],
    }

# --- Home Page ---
def home(request):
    try:
        profile = Profile.objects.filter(is_active=True).first()
        about = About.objects.filter(is_active=True).first()
        stats = Stats.objects.filter(is_active=True).first()
        resume = Resume.objects.filter(is_active=True).first()
        skill_categories = SkillCategory.objects.filter(is_active=True).prefetch_related('skills').order_by('order', 'name')
        educations = Education.objects.filter(is_active=True).order_by('-start_year', 'order')
        experiences = Experience.objects.filter(is_active=True).prefetch_related('responsibilities').order_by('-start_date', 'order')
        projects = Project.objects.filter(is_active=True, is_featured=True)[:6]
        services = Service.objects.filter(is_active=True)[:6]

        formatted_skill_categories = []
        for category in skill_categories:
            active_skills = category.skills.filter(is_active=True).order_by('order', 'name')
            if active_skills.exists():
                formatted_skill_categories.append({
                    'name': category.name,
                    'slug': category.slug,
                    'skills': [
                        {
                            'name': skill.name,
                            'image': skill.image.url if skill.image else '',
                            'percentage': skill.percentage
                        }
                        for skill in active_skills
                    ]
                })

        formatted_experiences = []
        for exp in experiences:
            formatted_experiences.append({
                'position': exp.position,
                'start_date': exp.start_date,
                'end_date': exp.end_date,
                'company': exp.company,
                'location': exp.location,
                'responsibilities': [
                    {'description': resp.description}
                    for resp in exp.responsibilities.all().order_by('order')
                ]
            })

        context = {
            'title': f'{profile.name} - Portfolio' if profile else 'Portfolio',
            'profile': {
                'name': profile.name if profile else '',
                'typed_items': profile.typed_items if profile else '',
                'website': profile.website if profile else '',
                'phone': profile.phone if profile else '',
                'city': profile.city if profile else '',
                'email': profile.email if profile else '',
                'freelance_status': profile.freelance_status if profile else '',
                'address': profile.address if profile else '',
                'twitter_url': profile.twitter_url if profile else '',
                'facebook_url': profile.facebook_url if profile else '',
                'instagram_url': profile.instagram_url if profile else '',
                'linkedin_url': profile.linkedin_url if profile else '',
                'teams_url': profile.teams_url if profile else '',
            } if profile else {},
            'about': {
                'description': about.description if about else '',
                'title': about.title if about else '',
                'detailed_description': about.detailed_description if about else '',
                'image': about.profile_image if about else '',
            } if about else {},
            'stats': {
                'happy_clients': stats.happy_clients if stats else 0,
                'projects': stats.projects if stats else 0,
                'support_hours': stats.support_hours if stats else 0,
                'team_members': stats.team_members if stats else 0,
            } if stats else {},
            'skill_categories': formatted_skill_categories,
            'resume': {
                'summary': resume.summary if resume else '',
                'pdf_file': resume.pdf_file.url if resume and resume.pdf_file else '',
            } if resume else {},
            'educations': [
                {
                    'degree': edu.degree,
                    'start_year': edu.start_year,
                    'end_year': edu.end_year,
                    'institution': edu.institution,
                    'location': edu.location,
                    'description': edu.description,
                }
                for edu in educations
            ],
            'experiences': formatted_experiences,
            'contact_info': {
                'address': profile.address if profile else '',
                'phone': profile.phone if profile else '',
                'email': profile.email if profile else '',
            } if profile else {},
            'projects': projects,
            'services': services,
        }
    except Exception as e:
        messages.warning(request, 'Database not configured. Using sample data.')
        context = get_fallback_context()
    return render(request, 'portfolio/home.html', context)

# --- About redirects to Home ---
def about(request):
    return redirect('portfolio:home')

# --- Projects List ---
def projects_list(request):
    projects = Project.objects.filter(is_active=True).order_by('-created_at')
    tech_filter = request.GET.get('tech')
    if tech_filter:
        projects = projects.filter(technologies__icontains=tech_filter)
    all_projects = Project.objects.filter(is_active=True)
    technologies = set()
    for project in all_projects:
        if project.technologies:
            techs = [tech.strip() for tech in project.technologies.split(',')]
            technologies.update(techs)
    context = {
        'projects': projects,
        'technologies': sorted(technologies),
        'current_tech_filter': tech_filter,
        'title': 'All Projects'
    }
    return render(request, 'portfolio/projects_list.html', context)

# --- Project Detail ---
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related_projects = Project.objects.filter(is_active=True).exclude(id=project.id)[:3]
    context = {
        'project': project,
        'related_projects': related_projects,
        'title': f'{project.title} - Project Details',
        'technologies': project.technologies.split(',') if project.technologies else []
    }
    return render(request, 'portfolio/project_detail.html', context)

# --- Services List ---
def services_list(request):
    services = Service.objects.filter(is_active=True).order_by('order', 'title')
    context = {
        'services': services,
        'title': 'Services'
    }
    return render(request, 'portfolio/services_list.html', context)

# --- Service Detail ---
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related_services = Service.objects.filter(is_active=True).exclude(id=service.id)[:3]
    context = {
        'service': service,
        'related_services': related_services,
        'title': f'{service.title} - Service Details'
    }
    return render(request, 'portfolio/service_detail.html', context)

# --- Contact redirects to Home ---
def contact(request):
    return redirect('portfolio:home')

# --- Contact Form Handler ---
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            if hasattr(settings, 'EMAIL_HOST') and settings.EMAIL_HOST:
                try:
                    profile = Profile.objects.filter(is_active=True).first()
                    admin_email = profile.email if profile else settings.DEFAULT_FROM_EMAIL
                    send_mail(
                        f'Portfolio Contact: {subject}',
                        f'From: {name} ({email})\n\nMessage:\n{message}',
                        settings.DEFAULT_FROM_EMAIL,
                        [admin_email],
                        fail_silently=False,
                    )
                except Exception as email_error:
                    print(f"Email sending failed: {email_error}")
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again.')
            print(f"Contact form error: {e}")
        return redirect('portfolio:home')
    return redirect('portfolio:home')

# --- Resume Download ---
def download_resume(request):
    resume = Resume.objects.filter(is_active=True).first()
    if resume and resume.pdf_file:
        try:
            with open(resume.pdf_file.path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="resume.pdf"'
                return response
        except FileNotFoundError:
            raise Http404("Resume file not found")
    else:
        messages.error(request, 'Resume not available for download.')
        return redirect('portfolio:home')
