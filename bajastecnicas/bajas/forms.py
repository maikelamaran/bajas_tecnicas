from django import forms
from . import models
from .choices import ESTADO_ACTUAL_CHOICES, ESTADO_CHOICES, MOTIVO_BAJA_CHOICES, DESTINO_FINAL_CHOICES, ANEXOS_CHOICES, UNIDAD_ORGANIZATIVA_CHOICES, DETALLES_CHOICES,AREA_PERTENECE
from django.contrib.auth.models import User

class BajasForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Recibe el usuario desde la vista
        super().__init__(*args, **kwargs)

        # Deshabilitar el campo responsable si no tiene permiso
        if user and not (user.is_superuser or user.has_perm("users.administrador_roles")):
            self.fields['responsable'].disabled = True
            self.fields['responsable'].help_text = "Solo los administradores de roles pueden modificar este campo."

    # Campos del formulario
    class Meta:
        model = models.Bajas
        fields = [
            "no_inv", "inm_herramienta", "denominacion_SAP", "unidad_org", "area_pertenece","fabricante","modelo","estado_actual","descripcion_est_actual","uso_actual","foto", "observaciones", 
            "estado", "motivo_baja", "destino_final", "años_explotacion", "valor_residual", 
            "detalle","argumento_deteriorado","argumento_obsoleto", "fecha_solicitud","archivo_anexo_0", "archivo_anexo_a", "archivo_anexo_a1","archivo_anexo_a2","archivo_anexo_a3", "archivo_mov_aft","responsable"
        ]
        

        widgets = {
            'no_inv': forms.TextInput(attrs={'class': 'form-control'}),
            'inm_herramienta': forms.TextInput(attrs={'class': 'form-control'}),
            'denominacion_SAP': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_org': forms.Select(attrs={'class': 'form-control'}, choices=UNIDAD_ORGANIZATIVA_CHOICES),
            'area_pertenece': forms.TextInput(attrs={'class': 'form-control'}),
            # 'equipo': forms.TextInput(attrs={'class': 'form-control'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_actual': forms.Select(attrs={'class': 'form-control'}, choices=ESTADO_ACTUAL_CHOICES),
            'descripcion_est_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'uso_actual': forms.TextInput(attrs={'class': 'form-control'}),
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
            'argumento_deteriorado': forms.TextInput(attrs={'class': 'form-control'}),
            'argumento_obsoleto': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_solicitud' : forms.DateInput(attrs={'type': 'date'}),
            'archivo_anexo_0': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'archivo_anexo_a': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'archivo_anexo_a1': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
            'archivo_anexo_a2': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
            'archivo_anexo_a3': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
                 
            'archivo_mov_aft': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
            'responsable': forms.Select(attrs={'class': 'form-control'})
        }

    # def clean_valor_residual(self):
    #     """Validación para asegurar que el valor residual es mayor que cero"""
    #     valor = self.cleaned_data.get('valor_residual')
    #     if valor <= 0:
    #         raise forms.ValidationError("El valor residual debe ser mayor que cero.")
    #     return valor

    def clean_años_explotacion(self):
        """Validación para asegurarse de que los años de explotación no sean negativos"""
        años = self.cleaned_data.get('años_explotacion')
        if años < 0:
            raise forms.ValidationError("Los años de explotación no pueden ser negativos.")
        return años

    def clean(self):
        cleaned_data = super().clean()
        print("VALIDANDO BAJA...") 
        no_inv = cleaned_data.get("no_inv")
        inm_herramienta = cleaned_data.get("inm_herramienta")

        # Si ya existe una baja con el mismo no_inv
        if no_inv:
            existe_noinv = models.Bajas.objects.filter(no_inv=no_inv)
            if self.instance.pk:
                existe_noinv = existe_noinv.exclude(pk=self.instance.pk)
            if existe_noinv.exists():
                self.add_error('no_inv', "Ya existe una baja con este número de inventario.")

        # Si ya existe una baja con el mismo inm_herramienta
        if inm_herramienta:
            existe_inm = models.Bajas.objects.filter(inm_herramienta=inm_herramienta)
            if self.instance.pk:
                existe_inm = existe_inm.exclude(pk=self.instance.pk)
            if existe_inm.exists():
                self.add_error('inm_herramienta', "Ya existe una baja con este número de herramienta.")

        return cleaned_data