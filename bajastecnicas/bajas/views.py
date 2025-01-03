import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models import Q
from datetime import datetime
from .models import Bajas
from .forms import BajasForm
from django.core.paginator import Paginator

# Create your views here.
def bajas_list(request):
    bajass = Bajas.objects.all()

    noinv_herramienta = request.GET.get('noinv')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    motivo_baja = request.GET.get('motivo_baja')
    destino_final = request.GET.get('destino_final')
    fecha_inicio_solic = request.GET.get('fecha_inicio_solic')
    fecha_fin_solic = request.GET.get('fecha_fin_solic')
    unidad_org = request.GET.get('unidad_org')
    anexo_a = request.GET.get('anexo_a')
    anexo_a1 = request.GET.get('anexo_a1')
    anexo_a2 = request.GET.get('anexo_a2')
    anexo_a3 = request.GET.get('anexo_a3')

    if noinv_herramienta:
        #bajas = bajas.filter(no_inv=noinv_herramienta)
        bajass = bajass.filter( models.Q(no_inv=noinv_herramienta) | models.Q(inm_herramienta=noinv_herramienta))  

    if fecha_inicio:
        bajass = bajass.filter(date__gte=datetime.strptime(fecha_inicio, '%Y-%m-%d'))
    
    if fecha_fin:
        bajass = bajass.filter(date__lte=datetime.strptime(fecha_fin, '%Y-%m-%d'))

    if fecha_inicio_solic:
        try:
            bajass = bajass.filter(fecha_solicitud__gte=datetime.strptime(fecha_inicio_solic, '%Y-%m-%d'))
        except ValueError:
            pass  # Si la fecha no es válida, no aplicar el filtro

    if fecha_fin_solic:
        try:
            bajass = bajass.filter(fecha_solicitud__lte=datetime.strptime(fecha_fin_solic, '%Y-%m-%d'))
        except ValueError:
            pass  # Si la fecha no es válida, no aplicar el filtro

    if estado:
        bajass = bajass.filter(estado=estado)

    if unidad_org:
        bajass = bajass.filter(unidad_org=unidad_org)
        
    if motivo_baja:
        bajass = bajass.filter(motivo_baja=motivo_baja)

    if destino_final:
        bajass = bajass.filter(destino_final=destino_final)

    if anexo_a:
        if anexo_a == 'si':
            bajass = bajass.filter(Q(archivo_anexo_a__isnull=False) & ~Q(archivo_anexo_a=''))
        elif anexo_a == 'no':
            bajass = bajass.filter(Q(archivo_anexo_a__isnull=True) | Q(archivo_anexo_a=''))

    if anexo_a1:
        if anexo_a1 == 'si':
            bajass = bajass.filter(Q(archivo_anexo_a1__isnull=False) & ~Q(archivo_anexo_a1=''))
        elif anexo_a1 == 'no':
            bajass = bajass.filter(Q(archivo_anexo_a1__isnull=True) | Q(archivo_anexo_a1=''))

    if anexo_a2:  # Si anexo_a2 tiene un valor
        bajass = bajass.filter(anexo_a2=anexo_a2)       

    if anexo_a3:
        bajass = bajass.filter(anexo_a3=anexo_a3)

    #paginador 

    paginator = Paginator(bajass, 3)
    page_number = request.GET.get('page')
    bajas = paginator.get_page(page_number)

    #fin paginador

    return render(request,'bajas/bajas_list.html',{'bajas':bajas})


def bajas_page(request,id):
    # return HttpResponse(slug)
    baja = get_object_or_404(Bajas, id=id)
    return render(request,'bajas/bajas_page.html',{'baja':baja})

def crear_baja(request):
    if request.method == 'POST':
        form = BajasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el objeto de la base de datos
            return redirect('bajas:list')  # Redirige después de un envío exitoso
    else:
        form = BajasForm()

    return render(request, 'bajas/crear_bajas.html', {'form': form})

def eliminar_baja(request,id):
    baja = get_object_or_404(Bajas, pk=id)
    if request.method == 'POST':
        baja.delete()
        return redirect('bajas:list')

def editar_baja(request, id):
    baja = get_object_or_404(Bajas, pk=id)
    is_ledesma = request.user.username.lower() == 'ledesma'
    if request.method == 'POST':
        form = BajasForm(request.POST, request.FILES, instance=baja)
        if form.is_valid():
            form.save()
            return redirect('bajas:list')
    else:
        form = BajasForm(instance=baja)
    return render(request, 'bajas/editar_bajas.html', {'form': form, 'baja': baja, 'is_ledesma': is_ledesma})


    