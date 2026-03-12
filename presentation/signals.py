import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Project

@receiver(post_delete, sender=Project)
def eliminar_archivo_post_delete(sender, instance, **kwargs):
    """Borra el archivo cuando se elimina el registro"""
    try:
        if instance.image and os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    
    except:
        print("Image can't be deleted")

@receiver(pre_save, sender=Project)
def borrar_archivo_al_actualizar(sender, instance, **kwargs):
    """Borra el archivo viejo cuando se sube uno nuevo"""
    if not instance.id:
        return False

    try:
        viejo_obj = Project.objects.get(pk=instance.id)
    except Project.DoesNotExist:
        return False

    if viejo_obj.image and viejo_obj.image != instance.image:
        if os.path.isfile(viejo_obj.image.path):
            os.remove(viejo_obj.image.path)