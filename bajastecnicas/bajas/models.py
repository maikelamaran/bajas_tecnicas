import os
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from . import choices

# Create your models here.
from django.db import models

class Bajas(models.Model):    
    no_inv = models.CharField( max_length=50,blank=True)
    inm_herramienta = models.CharField( max_length=50,blank=True)
    denominacion_SAP = models.CharField(max_length=100)
    unidad_org = models.CharField(max_length=100,default='',blank=True)    
    area_pertenece = models.TextField(default='',blank=True)#nuevo  
    # equipo = models.CharField( max_length=50,blank=True)#nuevo
    fabricante = models.CharField( max_length=50,blank=True)#nuevo
    modelo = models.CharField( max_length=50,blank=True)#nuevo
    estado_actual = models.CharField(max_length=100, default='',blank=True)
    descripcion_est_actual = models.CharField( max_length=50,blank=True)#nuevo
    uso_actual = models.CharField( max_length=50,blank=True)
    foto = models.ImageField(upload_to='uploaded/', blank=True, null=True)   
    observaciones = models.TextField(blank=True)
    estado = models.CharField(max_length=100, default='No Procede')#no procede o procede o en_espera
    motivo_baja = models.CharField(max_length=100,default='',blank=True)#Obsolescencia o deterioro
    destino_final = models.CharField(max_length=100,default='',blank=True)
    años_explotacion = models.IntegerField()
    valor_residual = models.DecimalField(max_digits=12, decimal_places=2)
    detalle = models.TextField(default='',blank=True)  
    argumento_deteriorado = models.CharField(max_length=100,blank=True) #TODO: hacer que solo salga con las opciones deteriorado 
    argumento_obsoleto = models.CharField(max_length=100,blank=True) #TODO: hacer que solo salga con las opciones obsoleto 
    date = models.DateTimeField(auto_now_add=True)
    fecha_solicitud = models.DateField(default=timezone.now)
    archivo_anexo_0 = models.FileField(upload_to='anexos/', blank=True, null=True)
    archivo_anexo_a = models.FileField(upload_to='anexos/', blank=True, null=True)
    archivo_anexo_a1 = models.FileField(upload_to='anexos/', blank=True, null=True)
    archivo_anexo_a2 = models.FileField(upload_to='anexos/', blank=True, null=True)
    archivo_anexo_a3 = models.FileField(upload_to='anexos/', blank=True, null=True)
    # anexo_a2 = models.TextField(blank=True)  
    # anexo_a3 = models.TextField(blank=True)    
    archivo_mov_aft = models.FileField(upload_to='anexos/', blank=True, null=True)
    anexo_0aprobado = models.BooleanField(default=True)
    listopara_anexo_A = models.BooleanField(default=False)#esto lo lleno en el proceso de crear el anterior anexo
    listopara_anexo_A1 = models.BooleanField(default=False)
    listopara_anexo_A2 = models.BooleanField(default=False)
    listopara_anexo_A3 = models.BooleanField(default=False)
    informacion_anexo_a_completa = models.BooleanField(default=False)
    informacion_anexo_a1_completa = models.BooleanField(default=False)
    informacion_anexo_a2_completa = models.BooleanField(default=False)
    informacion_anexo_a3_completa = models.BooleanField(default=False)
    aprobado_anexoA1 = models.BooleanField(default=False)#esto lo lleno en el proceso de aprobar dentro de cada proceso y lleva al llenar datos
    aprobado_anexoA = models.BooleanField(default=False)
    aprobado_anexoA2 = models.BooleanField(default=False)
    aprobado_anexoA3 = models.BooleanField(default=False)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rechazada = models.BooleanField(default=False)


    #de esta forma hago que las propiedades anexo_a, anexo_a1, a2, y a3 sean computados,
    #  o sea tomen valor en dependencia de otros campos
    @property
    def anexo_0(self):
        return 'si' if self.archivo_anexo_0 else 'no'

    @property
    def anexo_a(self):
        return 'si' if self.archivo_anexo_a else 'no'

    @property
    def anexo_a1(self):
        return 'si' if self.archivo_anexo_a1 else 'no'    

    @property
    def anexo_a2(self):
        return 'si' if self.archivo_anexo_a2 else 'no' 
    
    @property
    def anexo_a3(self):
        return 'si' if self.archivo_anexo_a3 else 'no' 
    
    @property
    def mov_aft(self):
        return 'si' if self.archivo_mov_aft else 'no'

    def save(self, *args, **kwargs):
        # Lógica de guardado adicional si es necesario
        super().save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #     if self.archivo_anexo_a:
    #         # Cambiar el nombre del archivo basado en el número de inventario, por ejemplo
    #         filename, ext = os.path.splitext(self.archivo_anexo_a.name)
    #         self.archivo_anexo_a.name = f"{self.no_inv}_anexoA{ext}"
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Baja de {self.denominacion_SAP}"

    #TODO revisar si hay forma de agregar un label a anexo a quiero agregar la palabra solicitud en el label