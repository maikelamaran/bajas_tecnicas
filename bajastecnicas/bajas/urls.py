from django.urls import path
from . import views


app_name= 'bajas'
urlpatterns = [
    path('', views.bajas_list,name="list"), 
    path('<int:id>', views.bajas_page,name="baja-page"), 
    path('crear-baja/', views.crear_baja, name="crear-baja"),
    path('<int:id>/eliminar',views.eliminar_baja,name='eliminar_baja'),
    path('<int:id>/editar',views.editar_baja,name='editar_baja'),                                
    path('<int:id>/exportar',views.exportar_pdf,name='exportar_pdf'),                                
]