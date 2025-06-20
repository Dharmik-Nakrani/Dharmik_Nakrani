from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile, About, Stats, SkillCategory, Skill, Education,
    Experience, ExperienceResponsibility, Resume
)

class Command(BaseCommand):
    help = 'Load initial portfolio data'

    def handle(self, *args, **options):
        # Create Profile
        profile, created = Profile.objects.get_or_create(
            name='Dharmik Nakrani',
            defaults={
                'typed_items': 'DevOps Engineer, Cloud Engineer, Freelancer',
                'website': 'dharmiknakrani.techopstechnologies.com',
                'phone': '+91 9067127486',
                'city': 'Gujarat, India',
                'email': 'DharmikN@hotmail.com',
                'freelance_status': 'Available',
                'address': 'Surat, Gujarat, India',
                'twitter_url': 'https://x.com/dharmiknakrani3',
                'facebook_url': 'https://www.facebook.com/profile.php?id=100076234926240',
                'instagram_url': 'https://www.instagram.com/dharmik__nakrani__',
                'linkedin_url': 'https://www.linkedin.com/in/dharmik-nakrani-6176211a3/',
                'teams_url': 'skype:dharmik.nakrani',
            }
        )
        
        # Create About
        about, created = About.objects.get_or_create(
            title='DevOps Engineer & Cloud Specialist',
            defaults={
                'profile_image': '/img/profile.jpg',
                'description': 'Passionate DevOps engineer with expertise in cloud technologies, automation, and modern infrastructure management.',
                'detailed_description': 'I specialize in DevOps practices, cloud infrastructure, and automation using modern tools and technologies. My goal is to create solutions that not only meet technical requirements but also provide excellent scalability and reliability.'
            }
        )
        
        # Create Stats
        stats, created = Stats.objects.get_or_create(
            defaults={
                'happy_clients': 25,
                'projects': 50,
                'support_hours': 500,
                'team_members': 5,
            }
        )
        
        # Create Resume
        resume, created = Resume.objects.get_or_create(
            defaults={
                'summary': 'Innovative and deadline-driven DevOps Engineer with 3+ years of experience designing and implementing scalable infrastructure solutions from initial concept to final deployment.'
            }
        )
        
        # Create Skill Categories and Skills
        skill_data = [
            {
                'name': 'DevOps',
                'skills': [
                    {'name': 'AWS', 'percentage': 70},
                    {'name': 'Azure', 'percentage': 50},
                    {'name': 'Terraform', 'percentage': 90},
                    {'name': 'Kubernetes', 'percentage': 70},
                    {'name': 'GCP', 'percentage': 50},
                    {'name': 'Digital Ocean', 'percentage': 65},
                    {'name': 'Helm', 'percentage': 70},
                ]
            },
            {
                'name': 'Monitoring',
                'skills': [
                    {'name': 'DataDog', 'percentage': 35},
                    {'name': 'ELK', 'percentage': 50},
                    {'name': 'Grafana', 'percentage': 90},
                    {'name': 'Prometheus', 'percentage': 85},
                    {'name': 'Loki', 'percentage': 85},
                    {'name': 'Rancher', 'percentage': 70},
                    {'name': 'Kibana', 'percentage': 50},
                ]
            },
            {
                'name': 'Tools',
                'skills': [
                    {'name': 'Jenkins', 'percentage': 95},
                    {'name': 'Apache', 'percentage': 80},
                    {'name': 'Nginx', 'percentage': 80},
                    {'name': 'Bitbucket', 'percentage': 90},
                    {'name': 'Gitea', 'percentage': 95},
                    {'name': 'Github', 'percentage': 90},
                    {'name': 'Gitlab', 'percentage': 80},
                    {'name': 'CircleCI', 'percentage': 60},
                    {'name': 'Sonarqube', 'percentage': 55},
                ]
            },
            {
                'name': 'Database',
                'skills': [
                    {'name': 'MySQL', 'percentage': 70},
                    {'name': 'PostgreSQL', 'percentage': 60},
                    {'name': 'MongoDB', 'percentage': 55},
                    {'name': 'Firebase', 'percentage': 80},
                    {'name': 'Supabase', 'percentage': 70},
                ]
            },
            {
                'name': 'Programming',
                'skills': [
                    {'name': 'Python', 'percentage': 60},
                    {'name': 'Flutter', 'percentage': 70},
                    {'name': 'Bash', 'percentage': 95},
                    {'name': 'Groovy', 'percentage': 85},
                ]
            },
        ]
        
        for idx, category_data in enumerate(skill_data):
            category, created = SkillCategory.objects.get_or_create(
                name=category_data['name'],
                defaults={'order': idx}
            )
            
            for skill_idx, skill_data in enumerate(category_data['skills']):
                Skill.objects.get_or_create(
                    category=category,
                    name=skill_data['name'],
                    defaults={
                        'percentage': skill_data['percentage'],
                        'order': skill_idx
                    }
                )
        
        # Create Education
        education, created = Education.objects.get_or_create(
            degree='Master of Computer Application',
            institution='Gujarat University',
            defaults={
                'start_year': '2020',
                'end_year': '2022',
                'location': 'Gujarat, India',
                'description': 'Specialized in software engineering and cloud technologies. Completed projects in various DevOps tools and cloud platforms.'
            }
        )
        
        # Create Experience
        experience, created = Experience.objects.get_or_create(
            position='DevOps Engineer',
            company='TechOps Technologies',
            defaults={
                'start_date': '2022',
                'end_date': 'Present',
                'location': 'Gujarat, India',
            }
        )
        
        # Create Experience Responsibilities
        responsibilities = [
            'Lead in the design, development, and implementation of cloud infrastructure using AWS and Azure',
            'Implement CI/CD pipelines using Jenkins, GitLab CI, and GitHub Actions',
            'Manage containerized applications using Docker and Kubernetes',
            'Monitor and maintain system performance using Grafana, Prometheus, and ELK stack',
        ]
        
        for idx, resp_text in enumerate(responsibilities):
            ExperienceResponsibility.objects.get_or_create(
                experience=experience,
                description=resp_text,
                defaults={'order': idx}
            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded portfolio data')
        )