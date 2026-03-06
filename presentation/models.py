import uuid
from django.db import models

class Service(models.Model):
    
    id = models.UUIDField(primary_key=True, unique=True, blank=False, null=False, default=uuid.uuid4, editable=False)
    name = models.CharField('Nombre', null=False, blank=False, default='Servicio')
    description = models.CharField('Descripción', max_length=200, null=False, blank=False)
    active = models.BooleanField('Activo/inactivo', default=True)
    
    
    class Meta:
        
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self) -> str:
        
        return f'{self.name}'


class Company(models.Model):
    
    id = models.UUIDField(primary_key=True, unique=True, blank=False, null=False, default=uuid.uuid4, editable=False)
    name = models.CharField('Nombre', blank=False, null=False, default='Nombre de empresa')
    main_service = models.CharField('Servicio principal', blank=False, null=False)
    city = models.CharField('Ciudad', blank=False, null=False)
    country = models.CharField('País', blank=False, null=False, default='Perú')
    registration_date = models.DateField('Fecha registro', auto_now=False, auto_now_add=True)
    active = models.BooleanField('Activo/inactivo', default=True)
    
    
    class Meta:
        
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self) -> str:
        
        return f'{self.name}'
    

class Project(models.Model):
    
    id = models.UUIDField(primary_key=True, unique=True, blank=False, default=uuid.uuid4, editable=False)
    title = models.CharField('Título', blank=False, null=False)
    description = models.TextField('Descripción', blank=False, null=True)
    weight = models.DecimalField('Peso', max_digits=10, decimal_places=2, blank=False, null=False)
    duration = models.IntegerField('Duración(días)', blank=False, null=False)
    project_start = models.DateField('Fecha de inicio', auto_now=False, auto_now_add=False)
    finished_project = models.DateField('Fecha de entrega', auto_now=False, auto_now_add=False)
    active = models.BooleanField('Activo/inactivo', default=True)
    
    company = models.ForeignKey(Company, default='Empresa', on_delete=models.SET_DEFAULT)
    service = models.ForeignKey(Service, default='Servicio', on_delete=models.SET_DEFAULT)
    
    
    class Meta:
        
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self)->str:
        
        return f'{self.title}'
    