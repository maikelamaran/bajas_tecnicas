from django import forms
from . import models
from .choices import ESTADO_ACTUAL_CHOICES,RECHAZADA_CHOICES, ESTADO_CHOICES, MOTIVO_BAJA_CHOICES, DESTINO_FINAL_CHOICES, UNIDAD_ORGANIZATIVA_CHOICES, DETALLES_CHOICES,AREA_PERTENECE
from django.contrib.auth.models import User

class BajasForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Recibe el usuario desde la vista
        super().__init__(*args, **kwargs)

        # Deshabilitar el campo responsable si no tiene permiso
        # if user and not (user.is_superuser or user.has_perm("users.administrador_roles")):
        #     self.fields['responsable'].disabled = True
        #     self.fields['responsable'].help_text = "Solo los administradores de roles pueden modificar este campo."
        # self.fields['rechazada'].help_text = "Una vez rechazada la solicitud pásela a <strong>No</strong> cuando vaya a llenar los campos que le faltaron."

        # # Actualizar las opciones de "detalle" basadas en el motivo de baja
        # motivo = None
        # if "motivo_baja" in self.data:
        #     motivo = self.data.get("motivo_baja")
        # elif self.instance and self.instance.pk:
        #     motivo = self.instance.motivo_baja  # cuando editas una baja ya existente

        # if motivo == "Obsolescencia":
        #     self.fields['detalle'].choices = [
        #         ('OBSOLETO REUTILIZABLE', 'OBSOLETO REUTILIZABLE'),
        #         ('OBSOLETO NO REUTILIZABLE', 'OBSOLETO NO REUTILIZABLE'),
        #     ]
        # elif motivo == "deterioro":
        #     self.fields['detalle'].choices = [
        #         ('DETERIORADO ÚTIL', 'DETERIORADO ÚTIL'),
        #         ('DETERIORADO NO ÚTIL', 'DETERIORADO NO ÚTIL'),
        #     ]
        # else:
        #     # default con "Elija uno"
        #     self.fields['detalle'].choices = [
        #         ('', 'Elija uno')
        #     ]

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            max_tamano = 1 * 1024 * 1024  # 2 MB, ajusta según lo que quieras permitir
            if foto.size > max_tamano:
                raise forms.ValidationError("La imagen excede el tamaño máximo permitido (1MB).")
        return foto
    
    #para que ayudar desde el back end que no puedas elegir argumento de deterioro si el motivo es obsolescencia y al reves
    def clean(self):
        cleaned_data = super().clean()
        motivo = (cleaned_data.get("motivo_baja") or "").lower()
        arg_det = cleaned_data.get("argumento_deteriorado")
        arg_obs = cleaned_data.get("argumento_obsoleto")

        if motivo == "obsolescencia":
            if arg_det:
                self.add_error("argumento_deteriorado", "No debe completar este campo cuando el motivo es Obsolescencia.")
            if not arg_obs:
                self.add_error("argumento_obsoleto", "Este campo es obligatorio cuando el motivo es Obsolescencia.")
        elif motivo == "deterioro":
            if arg_obs:
                self.add_error("argumento_obsoleto", "No debe completar este campo cuando el motivo es Deterioro.")
            if not arg_det:
                self.add_error("argumento_deteriorado", "Este campo es obligatorio cuando el motivo es Deterioro.")

        return cleaned_data


    # Campos del formulario
    class Meta:
        model = models.Bajas
        fields = [
            "no_inv", "inm_herramienta", "rechazada", "denominacion_SAP", "unidad_org", "area_pertenece", "fabricante","modelo","estado_actual","descripcion_est_actual","uso_actual","foto", "observaciones", 
            "estado", "motivo_baja","detalle", "destino_final", "años_explotacion", "valor_residual", "argumento_deteriorado","argumento_obsoleto", "fecha_solicitud", "responsable"
        ]
        labels = {
            "no_inv": "Número de inventario",
            "inm_herramienta": "Número de inmovilizado",
            "rechazada": "Rechazada",
            "denominacion_SAP": "Denominación SAP",
            "unidad_org": "Unidad Organizativa",
            "area_pertenece": "Área a la que pertenece",
            "fabricante": "Fabricante",
            "modelo": "Modelo",
            "estado_actual": "Estado actual",
            "descripcion_est_actual": "Descripción del estado actual",
            "uso_actual": "Uso actual",
            "foto": "Fotografía",
            "observaciones": "Observaciones",
            "estado": "Estado",
            "motivo_baja": "Motivo de baja",
            "detalle": "Detalles",
            "destino_final": "Destino final",
            "años_explotacion": "Años de explotación",
            "valor_residual": "Valor residual",            
            "argumento_deteriorado": "Argumento deteriorado",
            "argumento_obsoleto": "Argumento obsoleto",
            "fecha_solicitud": "Fecha de solicitud en SAP",
            "responsable": "Responsable",
        }
        

        widgets = {
            'no_inv': forms.TextInput(attrs={'class': 'form-control'}),
            'inm_herramienta': forms.TextInput(attrs={'class': 'form-control'}),
            'rechazada': forms.Select(attrs={'class': 'form-control'}, choices=RECHAZADA_CHOICES),
            'denominacion_SAP': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_org': forms.Select(attrs={'class': 'form-select'}, choices=UNIDAD_ORGANIZATIVA_CHOICES),
            'area_pertenece': forms.TextInput(attrs={'class': 'form-select'}),
            # 'equipo': forms.TextInput(attrs={'class': 'form-control'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_actual': forms.Select(attrs={'class': 'form-select'}, choices=ESTADO_ACTUAL_CHOICES),
            'descripcion_est_actual': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
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
            'detalle': forms.Select(attrs={'class': 'form-select'}, choices=DETALLES_CHOICES),
            'destino_final': forms.Select(attrs={'class': 'form-select'}, choices=DESTINO_FINAL_CHOICES),
            
            'años_explotacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_residual': forms.NumberInput(attrs={'class': 'form-control'}),
            
            'argumento_deteriorado': forms.TextInput(attrs={'class': 'form-control'}),
            'argumento_obsoleto': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_solicitud' : forms.DateInput(attrs={'type': 'date'}),
            # 'archivo_anexo_0': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # 'archivo_anexo_a': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # 'archivo_anexo_a1': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
            # 'archivo_anexo_a2': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
            # 'archivo_anexo_a3': forms.ClearableFileInput(attrs={'class': 'form-control'}),   
                 
             
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