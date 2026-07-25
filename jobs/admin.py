from django.contrib import admin
from .models import Job, Application, Profile

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'experience_level', 'department', 'salary_range', 'is_active', 'created_at')
    list_filter = ('job_type', 'experience_level', 'department', 'is_active')
    search_fields = ('title', 'company', 'description', 'requirements')
    list_editable = ('is_active',)
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected jobs as Active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected jobs as Inactive"


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate_name', 'candidate_email', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at', 'job__department')
    search_fields = ('candidate_name', 'candidate_email', 'cover_letter', 'job__title', 'job__company')
    list_editable = ('status',)
    readonly_fields = ('applied_at',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'phone')
