from django import forms
from . import models
from .choices import ESTADO_CHOICES, MOTIVO_BAJA_CHOICES, DESTINO_FINAL_CHOICES, ANEXOS_CHOICES, UNIDAD_ORGANIZATIVA_CHOICES, DETALLES_CHOICES

class BajasForm(forms.ModelForm):  


    # Campos del formulario
    class Meta:
        model = models.Bajas
        fields = [
            "no_inv", "inm_herramienta", "denominacion_SAP", "unidad_org",  "foto", "observaciones", 
            "estado", "motivo_baja", "destino_final", "años_explotacion", "valor_residual", 
            "detalle", "fecha_solicitud", "archivo_anexo_a", "archivo_anexo_a1", "anexo_a2", "anexo_a3", "archivo_mov_aft"
        ]

        widgets = {
            'no_inv': forms.TextInput(attrs={'class': 'form-control'}),
            'inm_herramienta': forms.TextInput(attrs={'class': 'form-control'}),
            'denominacion_SAP': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_org': forms.Select(attrs={'class': 'form-control'}, choices=UNIDAD_ORGANIZATIVA_CHOICES),
            # 'anexo_a1': forms.Select(attrs={'class': 'form-control'}, choices=ANEXOS_CHOICES),
            # 'anexo_a': forms.Select(attrs={'class': 'form-control'}, choices=ANEXOS_CHOICES),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # 'mov_aft': forms.Select(attrs={'class': 'form-control'}, choices=ANEXOS_CHOICES),
            # 'anexo_a2': forms.Select(attrs={'class': 'form-control'}, choices=ANEXOS_CHOICES),
            # 'anexo_a3': forms.Select(attrs={'class': 'form-control'}, choices=ANEXOS_CHOICES),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            # Asignamos las opciones correctamente desde las variables definidas dentro de la clase
            'estado': forms.Select(attrs={'class': 'form-select'}, choices=ESTADO_CHOICES),
            'motivo_baja': forms.Select(attrs={'class': 'form-select'}, choices=MOTIVO_BAJA_CHOICES),
            'destino_final': forms.Select(attrs={'class': 'form-select'}, choices=DESTINO_FINAL_CHOICES),
            
            'años_explotacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_residual': forms.NumberInput(attrs={'class': 'form-control'}),
            'detalle': forms.Select(attrs={'class': 'form-select'}, choices=DETALLES_CHOICES),
            'fecha_solicitud' : forms.DateInput(attrs={'type': 'date'}),
            'archivo_anexo_a': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'archivo_anexo_a1': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
            'anexo_a2': forms.TextInput(attrs={'class': 'form-control'}),        
            'anexo_a3': forms.TextInput(attrs={'class': 'form-control'}),        
            'archivo_mov_aft': forms.ClearableFileInput(attrs={'class': 'form-control'})       
   
        }

    def clean_valor_residual(self):
        """Validación para asegurar que el valor residual es mayor que cero"""
        valor = self.cleaned_data.get('valor_residual')
        if valor <= 0:
            raise forms.ValidationError("El valor residual debe ser mayor que cero.")
        return valor

    def clean_años_explotacion(self):
        """Validación para asegurarse de que los años de explotación no sean negativos"""
        años = self.cleaned_data.get('años_explotacion')
        if años < 0:
            raise forms.ValidationError("Los años de explotación no pueden ser negativos.")
        return años
