from django.shortcuts import render
from .models import Service, Project

def index(request):
    
    services = Service.objects.filter(active=True)
    context = {'services': services}
    
    return render(request, "index.html", context)

def projects(request):
    
    projects = Project.objects.filter(active=True).order_by('-finished_project')[:6]
    
    return render(request, "projects.html", {'projects': projects})