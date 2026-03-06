from django.urls import path
from .views import index, projects

urlpatterns = [
    path('', index),
    path('proyectos/', projects)
]