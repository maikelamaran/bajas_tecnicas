from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bajas'

urlpatterns = [
    path('', views.bajas_list, name="list"), 
    path('<int:id>', views.bajas_page, name="baja-page"), 
    path('crear-baja/', views.crear_baja, name="crear-baja"),
    path('<int:id>/eliminar', views.eliminar_baja, name='eliminar_baja'),
    path('<int:id>/editar', views.editar_baja, name='editar_baja'),                                 
    # path('<int:id>/exportar', views.exportar_pdf, name='exportar_pdf'), 
    path('<int:id>/subir_anexo/', views.subir_anexo_firmado, name='subir_anexo'),

    path('<int:id>/aprobar_anexoA/', views.aprobar_anexoA, name='aprobar_anexoA'),
    path('<int:id>/aprobar_anexoA1/', views.aprobar_anexoA1, name='aprobar_anexoA1'),
    path('<int:id>/aprobar_anexoA2/', views.aprobar_anexoA2, name='aprobar_anexoA2'),
    path('<int:id>/aprobar_anexoA3/', views.aprobar_anexoA3, name='aprobar_anexoA3'),
    
    # Para editar los datos del Anexo A
    
    
    # Ruta para el nuevo botón de crear el PDF del Anexo A (solo después de llenar los datos)
    path('<int:id>/crear_anexoA/', views.crear_anexoA, name='crear_anexoA'),
    path('<int:id>/crear_anexoA1/', views.crear_anexoA1, name='crear_anexoA1'),
    path('<int:id>/crear_anexoA2/', views.crear_anexoA2, name='crear_anexoA2'),
    path('<int:id>/crear_anexoA3/', views.crear_anexoA3, name='crear_anexoA3'),

    # Rutas para las versiones Anexo A1, A2, A3 si existen
    path('<int:id>/trabajar_anexoA/', views.trabajar_anexoA, name='trabajar_anexoA'),
    path('<int:id>/trabajar_anexoA1/', views.trabajar_anexoA1, name='trabajar_anexoA1'),
    path('<int:id>/trabajar_anexoA2/', views.trabajar_anexoA2, name='trabajar_anexoA2'),
    path('<int:id>/trabajar_anexoA3/', views.trabajar_anexoA3, name='trabajar_anexoA3'),

    path('cargar_excel_inv/', views.cargar_excel_inv, name='cargar_excel_inv'),    
    # Ruta para buscar inventarios
    path('buscar_inventario/', views.buscar_inventario, name='buscar_inventario'),  
    path('descargar_anexos/<int:id>/', views.descargar_anexos_zip, name='descargar_anexos'),                        
]

# Para servir archivos estáticos y de medios si estamos en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
