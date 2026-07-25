import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recruitment_system.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job

def seed():
    print("Seeding database...")

    # 1. Create superuser
    username = 'admin'
    email = 'admin@recruitment.com'
    password = 'admin1234'

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser: {username}")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully.")
    else:
        print(f"Superuser {username} already exists.")

    # 2. Create sample jobs
    jobs_data = [
        {
            'title': 'Senior Full-Stack Engineer',
            'company': 'QuantumTech',
            'location': 'Remote / San Francisco, CA',
            'job_type': 'Remote',
            'experience_level': 'Senior',
            'department': 'Engineering',
            'salary_range': '$140k - $180k',
            'description': 'We are looking for a Senior Full-Stack Engineer to join our core product team. You will be responsible for designing, building, and deploying highly scalable web applications, optimizing performance, and mentoring junior engineers. Our stack includes Django, React, PostgreSQL, and AWS.',
            'requirements': (
                "5+ years of experience with Python (Django or FastAPI) and JavaScript/TypeScript (React or Vue).\n"
                "Proven track record of building and managing production-scale APIs and microservices.\n"
                "Experience with database optimization, indexing, and schema design in PostgreSQL.\n"
                "Familiarity with cloud platforms (AWS, GCP) and containerization (Docker, Kubernetes).\n"
                "Excellent communication skills and passion for collaborating in a cross-functional team."
            ),
            'benefits': (
                "Premium health, dental, and vision insurance.\n"
                "Flexible work environment with remote-first culture.\n"
                "$2,000 annual home office & learning stipend.\n"
                "401(k) matching (4% fully vested from day one).\n"
                "Generous parental leave and unlimited paid time off."
            )
        },
        {
            'title': 'Lead Product Designer',
            'company': 'Aura Studio',
            'location': 'New York, NY',
            'job_type': 'Full-time',
            'experience_level': 'Lead / Lead Tech',
            'department': 'Design',
            'salary_range': '$130k - $160k',
            'description': 'Aura Studio is seeking an experienced Lead Product Designer to guide the user experience and visual aesthetic of our flagship platform. You will translate complex workflows into simple, elegant, and modern designs, establish our design system, and work closely with product managers and frontend engineers to bring your visions to life.',
            'requirements': (
                "6+ years of UI/UX design experience in SaaS or B2C web/mobile products.\n"
                "Strong portfolio demonstrating beautiful typography, visual systems, and user-centric problem solving.\n"
                "Proficiency in Figma, interactive prototyping, and design systems.\n"
                "Experience running usability studies and translating user feedback into design iterations.\n"
                "Familiarity with basic HTML/CSS is a plus."
            ),
            'benefits': (
                "Competitive base salary + equity packages.\n"
                "Stunning modern office space in Manhattan with fully stocked kitchen.\n"
                "Annual wellness allowance and gym membership discount.\n"
                "15 days of vacation + local holidays + company closure in winter."
            )
        },
        {
            'title': 'Junior Front-End Developer',
            'company': 'Vividly Interactive',
            'location': 'Hybrid / London, UK',
            'job_type': 'Full-time',
            'experience_level': 'Entry Level',
            'department': 'Engineering',
            'salary_range': '£45k - £55k',
            'description': 'Join our creative development team to build interactive, fast, and responsive user interfaces. This is a junior role where you will receive intensive mentorship, work directly on customer-facing features, and learn how to write clean, maintainable component code using modern JavaScript frameworks.',
            'requirements': (
                "1+ years of experience with HTML, CSS, and modern JavaScript.\n"
                "Basic understanding of React or Vue frameworks.\n"
                "Familiarity with Git/GitHub and collaborative developer workflows.\n"
                "Eagerness to learn, ask questions, and grow as a developer.\n"
                "Good problem-solving skills and attention to design details."
            ),
            'benefits': (
                "Comprehensive onboarding and mentoring program.\n"
                "Hybrid work options (2 days office, 3 days remote).\n"
                "Company-provided latest MacBook Pro and peripherals.\n"
                "Regular team building, dinners, and hackathons.\n"
                "Free access to online learning platforms."
            )
        },
        {
            'title': 'Technical Product Manager',
            'company': 'Nexus Flow',
            'location': 'Remote / Berlin, Germany',
            'job_type': 'Remote',
            'experience_level': 'Mid Level',
            'department': 'Product',
            'salary_range': '€75k - €95k',
            'description': 'We are looking for a Technical Product Manager to oversee the lifecycle of our core APIs and integration suite. You will bridge the gap between engineering teams and business stakeholders, write comprehensive product requirements, define the roadmap, and prioritize backlog items to deliver high-impact platform tools.',
            'requirements': (
                "3+ years of experience as a PM, technical BA, or engineer in software development.\n"
                "Deep understanding of APIs, software integrations, and web service architectures.\n"
                "Strong analytical skills, experience with SQL or data tools for decision making.\n"
                "Proven ability to manage stakeholder expectations and lead project delivery.\n"
                "Fluent English speaker with excellent written communication."
            ),
            'benefits': (
                "Work from anywhere in Europe.\n"
                "Stock option scheme.\n"
                "Annual company retreats in beautiful destinations.\n"
                "Language learning support and tuition reimbursement."
            )
        }
    ]

    for job in jobs_data:
        if not Job.objects.filter(title=job['title'], company=job['company']).exists():
            print(f"Creating job posting: {job['title']} at {job['company']}")
            Job.objects.create(**job)
        else:
            print(f"Job posting '{job['title']}' at '{job['company']}' already exists.")

    print("Seeding completed successfully.")

if __name__ == "__main__":
    seed()
