from django.urls import path
from .views import index, projects, contact

urlpatterns = [
    path('', index),
    path('proyectos/', projects),
    path('contacto/', contact)
]