from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Candidate', 'Candidate'),
        ('Employer', 'Employer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Candidate')
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        Profile.objects.create(user=instance)


class Job(models.Model):
    JOB_TYPES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    ]

    EXPERIENCE_LEVELS = [
        ('Entry Level', 'Entry Level'),
        ('Mid Level', 'Mid Level'),
        ('Senior', 'Senior'),
        ('Lead / Lead Tech', 'Lead / Lead Tech'),
    ]

    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs', null=True, blank=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES, default='Full-time')
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVELS, default='Mid Level')
    department = models.CharField(max_length=100, default='Engineering')
    salary_range = models.CharField(max_length=100, help_text='e.g., $100k - $130k', blank=True)
    description = models.TextField()
    requirements = models.TextField(help_text="Enter each requirement on a new line.")
    benefits = models.TextField(help_text="Enter each benefit on a new line.", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_requirements_list(self):
        return [r.strip() for r in self.requirements.split('\n') if r.strip()]

    def get_benefits_list(self):
        return [b.strip() for b in self.benefits.split('\n') if b.strip()]

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-created_at']


class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Screening', 'Screening'),
        ('Interview', 'Interview'),
        ('Offered', 'Offered'),
        ('Rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    candidate_name = models.CharField(max_length=200)
    candidate_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.candidate_name} for {self.job.title}"

    class Meta:
        ordering = ['-applied_at']
