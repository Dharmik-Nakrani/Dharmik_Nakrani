from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    # Sample data - you can replace this with database queries later
    context = {
        'title': 'Dharmik Nakrani - Portfolio',
        'profile': {
            'name': 'Dharmik Nakrani',
            'typed_items': 'DevOps Engineer, Cloud Engineer, Freelancer',
            'birthday': '22 May 2000',
            'website': 'dharmiknakrani.techopstechnologies.com',
            'phone': '+91 9067127486',
            'city': 'Gujarat, India',
            'age': '25',
            'degree': "Master of Computer Application",
            'email': 'DharmikN@hotmail.com',
            'freelance_status': 'Available',
            'address': 'Surat, Gujarat, India',
            'twitter_url': 'https://x.com/dharmiknakrani3',
            'facebook_url': 'https://www.facebook.com/profile.php?id=100076234926240',
            'instagram_url': 'https://www.instagram.com/dharmik__nakrani__',
            'linkedin_url': 'https://www.linkedin.com/in/dharmik-nakrani-6176211a3/',
            'teams_url': 'skype:dharmik.nakrani',
        },
        'about': {
            'description': 'Passionate full-stack developer with expertise in Django, React, and modern web technologies.',
            'title': 'Full Stack Developer & Software Engineer',
            'subtitle': 'Dedicated to creating efficient, scalable, and user-friendly applications.',
            'detailed_description': 'I specialize in developing web applications using Django, React, and modern JavaScript frameworks. My goal is to create solutions that not only meet technical requirements but also provide excellent user experiences.'
        },
        'stats': {
            'happy_clients': 25,
            'projects': 50,
            'support_hours': 500,
            'team_members': 5,
        },
        'skills_left': [
            {'name': 'Python', 'percentage': 90},
            {'name': 'Django', 'percentage': 85},
            {'name': 'JavaScript', 'percentage': 80},
        ],
        'skills_right': [
            {'name': 'React', 'percentage': 75},
            {'name': 'PostgreSQL', 'percentage': 80},
            {'name': 'Docker', 'percentage': 70},
        ],
        'resume': {
            'summary': 'Innovative and deadline-driven Software Developer with 3+ years of experience designing and developing user-centered web applications from initial concept to final, polished deliverable.'
        },
        'educations': [
            {
                'degree': 'Bachelor of Computer Science & Engineering',
                'start_year': '2018',
                'end_year': '2022',
                'institution': 'Mumbai University',
                'location': 'Mumbai, India',
                'description': 'Specialized in software engineering and web development. Completed projects in various programming languages and frameworks.'
            }
        ],
        'experiences': [
            {
                'position': 'Full Stack Developer',
                'start_date': '2022',
                'end_date': 'Present',
                'company': 'Tech Solutions Inc.',
                'location': 'Mumbai, India',
                'responsibilities': [
                    {'description': 'Lead in the design, development, and implementation of web applications using Django and React'},
                    {'description': 'Collaborate with cross-functional teams to deliver high-quality software solutions'},
                    {'description': 'Optimize application performance and ensure scalability'},
                    {'description': 'Mentor junior developers and conduct code reviews'},
                ]
            }
        ],
        'contact_info': {
            'address': 'Mumbai, Maharashtra, India',
            'phone': '+91 12345 67890',
            'email': 'dharmik@example.com',
        }
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    return redirect('portfolio:home')

def projects(request):
    return redirect('portfolio:home')

def contact(request):
    return redirect('portfolio:home')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you can add email sending logic
        try:
            # send_mail(
            #     f'Portfolio Contact: {subject}',
            #     f'From: {name} ({email})\n\nMessage:\n{message}',
            #     email,
            #     ['your-email@example.com'],
            #     fail_silently=False,
            # )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again.')
        
        return redirect('portfolio:home')
    
    return redirect('portfolio:home')

def project_detail(request, slug):
    # Placeholder for project detail view
    return render(request, 'portfolio/project_detail.html', {'slug': slug})

def service_detail(request, slug):
    # Placeholder for service detail view
    return render(request, 'portfolio/service_detail.html', {'slug': slug})
