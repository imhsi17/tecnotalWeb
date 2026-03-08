from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import Service, Project
from django.conf import settings
from django.contrib import messages

def index(request):
    
    services = Service.objects.filter(active=True)
    context = {'services': services}
    
    return render(request, "index.html", context)

def projects(request):
    
    projects = Project.objects.select_related('service', 'company').filter(active=True).order_by('-finished_project')[:6]
    
    return render(request, "projects.html", {'projects': projects})

def contact(request):

    if request.method == 'POST':
        name = request.POST['nombres']
        mail = request.POST['correo']
        phone = request.POST['celular']
        message = request.POST['mensaje']
        
        # Configuración del correo a enviar
        subject = f"Nuevo Contacto desde la Web: {name}"
        template = f"""
                    Has recibido un nuevo mensaje de contacto desde la página web Tecnotal.

                    Datos del Cliente:
                    - Nombres: {name}
                    - Correo: {mail}
                    - Número Celular: {phone}
                    -------------------------------------------------------------------------
                    {message}
                    """
        to = ['calderonhuaynates@gmail.com']     # Correo que recibe (El administrador)
        
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            to
        )
        
        email.send(fail_silently=False)
        
        messages.success(request, 'Se envío el correo. Pronto nos contactaremos contigo.')
        return render(request, "contact.html")
    
    return render(request, "contact.html")