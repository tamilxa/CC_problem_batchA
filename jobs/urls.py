from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/success/', views.application_success, name='application_success'),
    
    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/candidate/', views.dashboard_candidate, name='dashboard_candidate'),
    path('dashboard/employer/', views.dashboard_employer, name='dashboard_employer'),
    
    # Job Management
    path('job/add/', views.post_job, name='post_job'),
    path('job/<int:pk>/edit/', views.edit_job, name='edit_job'),
]
