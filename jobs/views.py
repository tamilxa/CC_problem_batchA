from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Job, Application, Profile
from .forms import ApplicationForm, SignupForm, JobForm

def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(requirements__icontains=search_query)
        )
        
    department = request.GET.get('department', '')
    if department:
        jobs = jobs.filter(department=department)
        
    job_type = request.GET.get('job_type', '')
    if job_type:
        jobs = jobs.filter(job_type=job_type)
        
    experience_level = request.GET.get('experience_level', '')
    if experience_level:
        jobs = jobs.filter(experience_level=experience_level)

    departments = Job.objects.filter(is_active=True).values_list('department', flat=True).distinct()
    job_types = Job.objects.filter(is_active=True).values_list('job_type', flat=True).distinct()
    experience_levels = Job.objects.filter(is_active=True).values_list('experience_level', flat=True).distinct()

    context = {
        'jobs': jobs,
        'departments': departments,
        'job_types': job_types,
        'experience_levels': experience_levels,
        'search_query': search_query,
        'selected_department': department,
        'selected_job_type': job_type,
        'selected_experience_level': experience_level,
    }
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            if request.user.is_authenticated:
                application.candidate = request.user
            application.save()
            return redirect('application_success', pk=job.pk)
    else:
        # Prepopulate name and email if logged in
        initial_data = {}
        if request.user.is_authenticated:
            initial_data['candidate_name'] = f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username
            initial_data['candidate_email'] = request.user.email
        form = ApplicationForm(initial=initial_data)
        
    context = {
        'job': job,
        'form': form,
    }
    return render(request, 'jobs/job_detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            
            # Update the automatically created profile role
            user.profile.role = form.cleaned_data.get('role')
            user.profile.save()
            
            login(request, user)
            messages.success(request, f"Account created successfully for {user.username}!")
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.profile.role == 'Employer':
        return redirect('dashboard_employer')
    else:
        return redirect('dashboard_candidate')

@login_required
def dashboard_candidate(request):
    applications = Application.objects.filter(candidate=request.user)
    return render(request, 'jobs/dashboard_candidate.html', {'applications': applications})

@login_required
def dashboard_employer(request):
    jobs = Job.objects.filter(employer=request.user)
    # Collect all applications for jobs posted by this employer
    applications = Application.objects.filter(job__employer=request.user)
    
    # Handle status change if submitted via POST
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        new_status = request.POST.get('status')
        if app_id and new_status:
            application = get_object_or_404(Application, pk=app_id, job__employer=request.user)
            application.status = new_status
            application.save()
            messages.success(request, f"Updated status of {application.candidate_name} to {new_status}.")
            return redirect('dashboard_employer')

    context = {
        'jobs': jobs,
        'applications': applications,
        'status_choices': Application.STATUS_CHOICES,
    }
    return render(request, 'jobs/dashboard_employer.html', context)

@login_required
def post_job(request):
    if request.user.profile.role != 'Employer':
        messages.error(request, "Only employers can post jobs.")
        return redirect('job_list')
        
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            messages.success(request, f"Job posting '{job.title}' created successfully!")
            return redirect('dashboard_employer')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Post a New Job'})

@login_required
def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk, employer=request.user)
    
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, f"Job posting '{job.title}' updated successfully!")
            return redirect('dashboard_employer')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form, 'title': f'Edit {job.title}'})

def application_success(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/application_success.html', {'job': job})

def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect('job_list')
