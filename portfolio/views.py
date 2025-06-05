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
            'typed_items': 'Developer, Designer, Freelancer, Problem Solver',
            'birthday': '1 Jan 1995',
            'website': 'www.dharmik.dev',
            'phone': '+91 12345 67890',
            'city': 'Mumbai, India',
            'age': '25',
            'degree': "Bachelor's in Computer Science",
            'email': 'dharmik@example.com',
            'freelance_status': 'Available',
            'address': 'Mumbai, Maharashtra, India',
            'twitter_url': 'https://twitter.com/dharmik',
            'facebook_url': 'https://facebook.com/dharmik',
            'instagram_url': 'https://instagram.com/dharmik',
            'linkedin_url': 'https://linkedin.com/in/dharmik',
            'skype_url': 'skype:dharmik.nakrani',
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
