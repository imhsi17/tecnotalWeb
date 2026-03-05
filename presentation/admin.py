from django.contrib import admin
from .models import Service, Project, Company

# Register your models here.

@admin.register(Service)
class SericeAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'description', 'active', )
    list_filter = ('active', )
    search_fields = ['name', ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'main_service', 'registration_date', 'city', 'country', 'active', )
    list_filter = ('active', 'main_service', )
    search_fields = ('name', )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'weight', 'duration', 'project_start', 'finished_project', 'active', )
    list_filter = ('active', )
    search_fields = ('title', )
