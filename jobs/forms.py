from django import forms
from django.contrib.auth.models import User
from .models import Application, Job, Profile

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['candidate_name', 'candidate_email', 'resume', 'cover_letter']
        widgets = {
            'candidate_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your full name'
            }),
            'candidate_email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your.email@example.com'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-file-input',
                'accept': '.pdf,.doc,.docx'
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Tell us why you are a great fit for this role...',
                'rows': 5
            }),
        }


class SignupForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('Candidate', 'Candidate'),
        ('Employer', 'Employer'),
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'filter-select'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Create password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirm password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Choose username'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'you@example.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
        return cleaned_data


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'company', 'location', 'job_type', 
            'experience_level', 'department', 'salary_range', 
            'description', 'requirements', 'benefits'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Senior Python Developer'}),
            'company': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Tech Corp'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Remote or San Francisco, CA'}),
            'job_type': forms.Select(attrs={'class': 'filter-select'}),
            'experience_level': forms.Select(attrs={'class': 'filter-select'}),
            'department': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Engineering, Design'}),
            'salary_range': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., $100k - $120k'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Describe the role...', 'rows': 5}),
            'requirements': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Enter requirements, each on a new line...', 'rows': 5}),
            'benefits': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Enter benefits, each on a new line...', 'rows': 5}),
        }
