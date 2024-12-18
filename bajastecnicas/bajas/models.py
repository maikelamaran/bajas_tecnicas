from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Bajas(models.Model):    
    no_inv = models.CharField( max_length=50,blank=True)
    inm_herramienta = models.CharField( max_length=50,blank=True)
    denominacion_SAP = models.CharField(max_length=100)
    unidad_org = models.TextField()    
    foto = models.ImageField(upload_to='uploaded/', blank=True, null=True)   
    observaciones = models.TextField(blank=True)
    estado = models.CharField(max_length=100)#no procede o procede o en_espera
    motivo_baja = models.CharField(max_length=100)#obsolencia o deterioro
    destino_final = models.TextField()
    años_explotacion = models.IntegerField()
    valor_residual = models.DecimalField(max_digits=12, decimal_places=2)
    detalle = models.TextField(default='DETERIORADO ÚTIL')    
    date = models.DateTimeField(auto_now_add=True)
    fecha_solicitud = models.DateField(default=timezone.now)
    archivo_anexo_a = models.FileField(upload_to='anexos/', blank=True, null=True)
    archivo_anexo_a1 = models.FileField(upload_to='anexos/', blank=True, null=True)
    anexo_a2 = models.TextField(blank=True)  
    anexo_a3 = models.TextField(blank=True)  
    archivo_mov_aft = models.FileField(upload_to='anexos/', blank=True, null=True)


    #de esta forma hago que las propiedades anexo_a, anexo_a1, a2, y a3 sean computados,
    #  o sea tomen valor en dependencia de otros campos
    @property
    def anexo_a(self):
        return 'si' if self.archivo_anexo_a else 'no'

    @property
    def anexo_a1(self):
        return 'si' if self.archivo_anexo_a1 else 'no'    

    @property
    def mov_aft(self):
        return 'si' if self.archivo_mov_aft else 'no'

    def save(self, *args, **kwargs):
        # Lógica de guardado adicional si es necesario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Baja de {self.denominacion_SAP}"

    #TODO revisar si hay forma de agregar un label a anexo a quiero agregar la palabra solicitud en el label