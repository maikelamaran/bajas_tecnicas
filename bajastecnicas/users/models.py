from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model

class DummyModel(models.Model):
    # Este modelo es solo para tener un ContentType donde colgar los permisos
    class Meta:
        permissions = [
            ("administrador_roles", "Administrador de roles"),
            ("aprobar_anexo_a", "Puede aprobar anexo A"),
            ("aprobar_anexo_a1", "Puede aprobar anexo A1"),
            ("aprobar_anexo_a2", "Puede aprobar anexo A2"),
            ("aprobar_anexo_a3", "Puede aprobar anexo A3"),
            ("llenar_anexo_a", "Puede llenar anexo A"),
            ("llenar_anexo_a1", "Puede llenar anexo A1"),
            ("llenar_anexo_a2", "Puede llenar anexo A2"),
            ("llenar_anexo_a3", "Puede llenar anexo A3"),
            ("crear_anexo_a", "Puede crear anexo A"),
            ("crear_anexo_a1", "Puede crear anexo A1"),
            ("crear_anexo_a2", "Puede crear anexo A2"),
            ("crear_anexo_a3", "Puede crear anexo A3"),
        ]
