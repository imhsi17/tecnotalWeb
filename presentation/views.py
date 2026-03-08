from django.shortcuts import render
from django.core.mail import send_mail
from .models import Service, Project

def index(request):
    
    services = Service.objects.filter(active=True)
    context = {'services': services}
    
    return render(request, "index.html", context)

def projects(request):
    
    projects = Project.objects.select_related('service', 'company').filter(active=True).order_by('-finished_project')[:6]
    
    return render(request, "projects.html", {'projects': projects})

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('nombres')
        mail = request.POST.get('correo')
        phone = request.POST.get('celular')
        
        # Configuración del correo a enviar
        asunto = f"Nuevo Contacto desde la Web: {name}"
        mensaje = f"""
Has recibido un nuevo mensaje de contacto desde la página web Tecnotal.

Datos del Cliente:
- Nombres: {name}
- Correo: {mail}
- Número Celular: {phone}
"""
        remitente = 'no-responder@tecnotal.com.pe' # Correo que envía
        destinatarios = ['informes@tecnotal.com.pe']     # Correo que recibe (El administrador)
        
        # Enviar el correo
        send_mail(asunto, mensaje, remitente, destinatarios, fail_silently=False)
        
        print(f"[{request.method}] Correo de contacto enviado desde {mail}")
    
    return render(request, "contact.html")