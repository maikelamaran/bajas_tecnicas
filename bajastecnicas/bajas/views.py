import datetime
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models import Q
from datetime import datetime
from .models import Bajas
from .forms import BajasForm
from django.core.paginator import Paginator
import os
from django.conf import settings

from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
import base64
from django.core.files.storage import default_storage
from .choices import ESTADO_CHOICES
import openpyxl
from django.http import JsonResponse
import pandas as pd
from django.http import JsonResponse
from datetime import datetime
from django.templatetags.static import static
from django.contrib import messages
import os
# Create your views here.


def bajas_list(request):
    puede_admin_roles = request.user.is_superuser or request.user.has_perm("users.administrador_roles")
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

        # bajas = bajas.filter(no_inv=noinv_herramienta)
        bajass = bajass.filter(models.Q(no_inv=noinv_herramienta) | models.Q(
            inm_herramienta=noinv_herramienta))

    if fecha_inicio:
        bajass = bajass.filter(
            date__gte=datetime.strptime(fecha_inicio, '%Y-%m-%d'))


    if fecha_fin:
        bajass = bajass.filter(
            date__lte=datetime.strptime(fecha_fin, '%Y-%m-%d'))

    if fecha_inicio_solic:
        try:
            bajass = bajass.filter(fecha_solicitud__gte=datetime.strptime(
                fecha_inicio_solic, '%Y-%m-%d'))
        except ValueError:
            pass  # Si la fecha no es válida, no aplicar el filtro

    if fecha_fin_solic:
        try:
            bajass = bajass.filter(
                fecha_solicitud__lte=datetime.strptime(fecha_fin_solic, '%Y-%m-%d'))
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
            bajass = bajass.filter(
                Q(archivo_anexo_a__isnull=False) & ~Q(archivo_anexo_a=''))
        elif anexo_a == 'no':
            bajass = bajass.filter(
                Q(archivo_anexo_a__isnull=True) | Q(archivo_anexo_a=''))

    if anexo_a1:
        if anexo_a1 == 'si':
            bajass = bajass.filter(
                Q(archivo_anexo_a1__isnull=False) & ~Q(archivo_anexo_a1=''))
        elif anexo_a1 == 'no':
            bajass = bajass.filter(
                Q(archivo_anexo_a1__isnull=True) | Q(archivo_anexo_a1=''))

    if anexo_a2:  # Si anexo_a2 tiene un valor
        bajass = bajass.filter(anexo_a2=anexo_a2)

    if anexo_a3:
        bajass = bajass.filter(anexo_a3=anexo_a3)



    bajass = bajass.order_by('id')
    paginator = Paginator(bajass, 3)
    page_number = request.GET.get('page')
    bajas = paginator.get_page(page_number)

    context = {
        "bajas": bajas,
        "puede_aprobar_anexo_a": request.user.has_perm("users.aprobar_anexo_a"),
        "puede_llenar_anexo_a": request.user.has_perm("users.llenar_anexo_a"),
        "puede_crear_anexo_a": request.user.has_perm("users.crear_anexo_a"),

        "puede_aprobar_anexo_a1": request.user.has_perm("users.aprobar_anexo_a1"),
        "puede_llenar_anexo_a1": request.user.has_perm("users.llenar_anexo_a1"),
        "puede_crear_anexo_a1": request.user.has_perm("users.crear_anexo_a1"),

        "puede_aprobar_anexo_a2": request.user.has_perm("users.aprobar_anexo_a2"),
        "puede_llenar_anexo_a2": request.user.has_perm("users.llenar_anexo_a2"),
        "puede_crear_anexo_a2": request.user.has_perm("users.crear_anexo_a2"),

        "puede_aprobar_anexo_a3": request.user.has_perm("users.aprobar_anexo_a3"),
        "puede_llenar_anexo_a3": request.user.has_perm("users.llenar_anexo_a3"),
        "puede_crear_anexo_a3": request.user.has_perm("users.crear_anexo_a3"),
        "puede_admin_roles": puede_admin_roles,
    }

    # fin paginador

    return render(request, 'bajas/bajas_list.html', context)


def bajas_page(request, id):
    # return HttpResponse(slug)
    baja = get_object_or_404(Bajas, id=id)
    return render(request, 'bajas/bajas_page.html', {'baja': baja})


def crear_baja(request):
    if request.method == 'POST':
        # Asegúrate de incluir request.FILES para manejar imágenes
        form = BajasForm(request.POST, request.FILES)

        # Si el formulario es válido
        if form.is_valid():
            # Guardar la baja en la base de datos
            baja = form.save()

            # Generar el PDF automáticamente
            context = {'baja': baja,
                       "logo_etecsa": request.build_absolute_uri(static('bajastecnicas/icons/etecsa_logo.jpeg'))}
            html_string = render_to_string('bajas/anexo_a.html', context)
            html_string_a0 = render_to_string('bajas/anexo_0.html', context)
            
            pdf_path_0 = f'anexos/anexo_{baja.id}_A0.pdf'
            

            with default_storage.open(pdf_path_0, 'wb') as pdf_file:
                pisa_status = pisa.CreatePDF(html_string_a0, dest=pdf_file)
                if pisa_status.err:
                    return render(request, 'bajas/error.html', {'mensaje': 'Error al generar el PDF a0'})           
            baja.archivo_anexo_0 = pdf_path_0
            baja.listopara_anexo_A = True            
            baja.save()            
            return redirect('bajas:list')
    else:
        form = BajasForm()

    # Cargar el archivo Excel para autocompletar los campos
    excel_path = os.path.join(settings.MEDIA_ROOT, 'uploaded/inventario.xlsx')

    try:
        # Leer el archivo Excel
        df = pd.read_excel(excel_path)

        # Limpiar los nombres de las columnas para eliminar posibles espacios
        df.columns = df.columns.str.strip()

        # Acceder a la lista de 'No_inventario' usando su columna C (índice 2)
        no_inv_list = df.iloc[:, 5].drop_duplicates().head(
            5).tolist()  # Columna C (índice 2)

    except Exception as e:
        # Si hay un error con el archivo Excel, se puede capturar y manejar adecuadamente
        no_inv_list = []
        print(f"Error al leer el archivo Excel: {e}")

    return render(request, 'bajas/crear_bajas.html', {
        'form': form,
        'no_inv_list': no_inv_list,  # Lista de números de inventario a enviar a la plantilla
    })


def eliminar_baja(request, id):
    is_ledesma = request.user.username.lower() == 'ledesma'
    baja = get_object_or_404(Bajas, pk=id)

    if request.method == 'POST':  # verifica si el método es POST
        if is_ledesma:  # Si el usuario es 'ledesma', permite la eliminación
            baja.delete()
            # Redirige a la lista después de eliminar
            return redirect('bajas:list')
        else:
            # Si no es 'ledesma', muestra el acceso denegado
            return render(request, 'bajas/acceso_denegado.html')

    # Si no es POST, también puede manejarse aquí (aunque generalmente los formularios de eliminación usan POST)
    return render(request, 'bajas/acceso_denegado.html')


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


def image_to_base64(image_path):
    with default_storage.open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


def exportar_pdf(request, id):
    baja = get_object_or_404(Bajas, id=id)
    if baja.foto:
        img_data = image_to_base64(baja.foto.path)
        img_tag = f"data:image/jpeg;base64,{img_data}"
    else:
        img_tag = None

    # Generar el HTML que va a ser convertido a PDF
    context = {'baja': baja, 'img_tag': img_tag}
    html_string = render_to_string('bajas/pdf_template.html', context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="baja_{baja.id}.pdf"'

    pisa_status = pisa.CreatePDF(html_string, dest=response)

    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF', status=400)

    return response


@login_required
def subir_anexo_firmado(request, id):
    baja = get_object_or_404(Bajas, id=id)

    if request.user.username.lower() != 'vladimir':
        return HttpResponse('No tiene permisos para realizar esta acción', status=403)

    if request.method == 'POST' and request.FILES.get('archivo_firmado'):
        archivo_firmado = request.FILES['archivo_firmado']

        # Sobrescribir el archivo PDF con el firmado
        baja.archivo_anexo_0 = archivo_firmado
        baja.estado = 'Firmado Anexo0'  # Cambia el estado
        baja.save()

        # Redirige a la lista después de subir el PDF
        return redirect('bajas:list')

    return render(request, 'bajas/subir_anexo.html', {'baja': baja})


def buscar_inventario(request):
    no_inv = request.GET.get('no_inv')

    if no_inv:
        excel_path = os.path.join(
            settings.MEDIA_ROOT, 'uploaded/inventario.xlsx')

        try:
            df = pd.read_excel(excel_path)
            df.columns = df.columns.str.strip()

            row = df[df.iloc[:, 2] == no_inv].iloc[0]
            denominacion_SAP = str(row.iloc[5]).strip()

            def clean_value(value):
                if pd.isna(value) or str(value).strip() == '':
                    return 0.0
                value = str(value).strip().replace(',', '')
                return float(value)

            valor_explotacion1 = clean_value(row.iloc[12])
            valor_explotacion2 = clean_value(row.iloc[14])
            valor_residual = valor_explotacion1 + valor_explotacion2
            centro_coste = str(row.iloc[9]).strip()
            local = str(row.iloc[11]).strip()
            area_pertenece = centro_coste + '/' + local
            # Calcular años de explotación
            fecha_explotacion_str = str(
                row.iloc[19]).strip()  # Ej: '14.08.2012'
            # fabricante = str(row.iloc[17]).strip()
            # modelo = str(row.iloc[18]).strip()
            inm_herramienta = str(row.iloc[1]).strip()

            if fecha_explotacion_str and fecha_explotacion_str != 'nan':
                try:
                    # Convertir la fecha en objeto datetime
                    fecha_explotacion = datetime.strptime(
                        fecha_explotacion_str, '%d.%m.%Y')

                    # Calcular la diferencia en años
                    fecha_actual = datetime.now()
                    diferencia = fecha_actual - fecha_explotacion
                    años_explotacion = diferencia.days // 365  # Aprox. en años
                except ValueError:
                    años_explotacion = None  # En caso de formato incorrecto
            else:
                años_explotacion = None

            return JsonResponse({
                'denominacion_SAP': denominacion_SAP,
                'valor_residual': valor_residual,
                'años_explotacion': años_explotacion,
                'area_pertenece': area_pertenece,
                # 'fabricante': fabricante,
                # 'modelo': modelo,
                'inm_herramienta': inm_herramienta
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Número de inventario no proporcionado'}, status=400)

@login_required
def aprobar_anexoA(request, id):
    baja = get_object_or_404(Bajas, id=id)
    baja.aprobado_anexoA = True
    baja.save()
    messages.success(request, "¡¡Aprobado el Anexo A!")
    return redirect('bajas:list')

@login_required
def aprobar_anexoA1(request, id):
    baja = get_object_or_404(Bajas, id=id)
    baja.aprobado_anexoA1 = True
    baja.save()
    messages.success(request, "¡¡Aprobado el Anexo A1!")
    return redirect('bajas:list')

@login_required
def aprobar_anexoA2(request, id):
    baja = get_object_or_404(Bajas, id=id)
    baja.aprobado_anexoA2 = True
    baja.save()
    messages.success(request, "¡Aprobado el Anexo A2!")
    return redirect('bajas:list')

@login_required
def aprobar_anexoA3(request, id):
    baja = get_object_or_404(Bajas, id=id)
    baja.aprobado_anexoA3 = True
    baja.save()
    messages.success(request, "¡¡Aprobado el Anexo A3!")
    return redirect('bajas:list')

@login_required
def trabajar_anexoA(request, id):
    baja = get_object_or_404(Bajas, pk=id)
    is_ledesma = request.user.username.lower() == 'ledesma'

    if request.method == 'POST':
        form = BajasForm(request.POST, request.FILES, instance=baja)
        if form.is_valid():  
            baja = form.save(commit=False)
            baja.informacion_anexo_a_completa = True
            baja.save()
            return redirect('bajas:list')
    else:
        form = BajasForm(instance=baja)

    return render(request, 'bajas/editar_bajas.html', {'form': form, 'baja': baja, 'is_ledesma': is_ledesma})

@login_required
def crear_anexoA(request, id):
    baja = get_object_or_404(Bajas, pk=id)  # Obtener la baja
    if not baja.informacion_anexo_a_completa:
        # Si la información no ha sido completada, redirigir o mostrar un error
        return redirect('bajas:trabajar_anexoA', id=id)

    # Generación del PDF
    print(f"Generando PDF para Anexo A...")

    context = {
        'baja': baja,
        "logo_etecsa": request.build_absolute_uri(static('bajastecnicas/icons/etecsa_logo.jpeg'))
    }

    html_string = render_to_string('bajas/anexo_a.html', context)

    pdf_path = f'anexos/anexo_{baja.id}_A.pdf'
    try:
        with default_storage.open(pdf_path, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

            if pisa_status.err:
                raise Exception("Error al generar el PDF")

        # Guardar la ruta del archivo PDF en el modelo
        baja.archivo_anexo_a = pdf_path
        baja.listopara_anexo_A1 = True
        
        baja.save()

        print(f"PDF generado con éxito y guardado en: {pdf_path}")

        return redirect('bajas:list')  # Redirigir al listado de bajas después de crear el PDF

    except Exception as e:
        print(f"Error al generar el PDF: {e}")
        return render(request, 'bajas/error.html', {'mensaje': 'Error al generar el PDF'})

@login_required
def trabajar_anexoA1(request, id):
    baja = get_object_or_404(Bajas, pk=id)
    is_ledesma = request.user.username.lower() == 'ledesma'

    if request.method == 'POST':
        form = BajasForm(request.POST, request.FILES, instance=baja)
        if form.is_valid():  
            baja = form.save(commit=False)
            baja.informacion_anexo_a1_completa = True
            baja.save()
            return redirect('bajas:list')
    else:
        form = BajasForm(instance=baja)

    return render(request, 'bajas/editar_bajas.html', {'form': form, 'baja': baja, 'is_ledesma': is_ledesma})

@login_required
def crear_anexoA1(request, id):
    baja = get_object_or_404(Bajas, pk=id)  # Obtener la baja
    if not baja.informacion_anexo_a1_completa:
        # Si la información no ha sido completada, redirigir o mostrar un error
        return redirect('bajas:trabajar_anexoA1', id=id)

    # Generación del PDF
    print(f"Generando PDF para Anexo A1...")

    context = {
        'baja': baja,
        "logo_etecsa": request.build_absolute_uri(static('bajastecnicas/icons/etecsa_logo.jpeg'))
    }

    html_string_a1 = render_to_string('bajas/anexo_a1.html', context)

    pdf_path_a1 = f'anexos/anexo_{baja.id}_A1.pdf'
    try:
        with default_storage.open(pdf_path_a1, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(html_string_a1, dest=pdf_file)

            if pisa_status.err:
                raise Exception("Error al generar el PDF")

        # Guardo la ruta del archivo PDF en el modelo
        baja.archivo_anexo_a1 = pdf_path_a1
        baja.listopara_anexo_A2 = True
        
        baja.save()

        print(f"PDF generado con éxito y guardado en: {pdf_path_a1}")

        return redirect('bajas:list') 

    except Exception as e:
        print(f"Error al generar el PDF: {e}")
        return render(request, 'bajas/error.html', {'mensaje': 'Error al generar el PDF'})

@login_required
def trabajar_anexoA2(request, id):
    baja = get_object_or_404(Bajas, pk=id)
    is_ledesma = request.user.username.lower() == 'ledesma'

    if request.method == 'POST':
        form = BajasForm(request.POST, request.FILES, instance=baja)
        if form.is_valid():  
            baja = form.save(commit=False)
            baja.informacion_anexo_a2_completa = True
            baja.save()
            return redirect('bajas:list')
    else:
        form = BajasForm(instance=baja)

    return render(request, 'bajas/editar_bajas.html', {'form': form, 'baja': baja, 'is_ledesma': is_ledesma})

@login_required
def crear_anexoA2(request, id):
    baja = get_object_or_404(Bajas, pk=id)  # Obtener la baja
    if not baja.informacion_anexo_a2_completa:
        # Si la información no ha sido completada, redirigir o mostrar un error
        return redirect('bajas:trabajar_anexoA2', id=id)

    # Generación del PDF
    print(f"Generando PDF para Anexo A2...")

    context = {
        'baja': baja,
        "logo_etecsa": request.build_absolute_uri(static('bajastecnicas/icons/etecsa_logo.jpeg'))
    }

    html_string_a2 = render_to_string('bajas/anexo_a2.html', context)

    pdf_path_a2 = f'anexos/anexo_{baja.id}_A2.pdf'
    try:
        with default_storage.open(pdf_path_a2, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(html_string_a2, dest=pdf_file)

            if pisa_status.err:
                raise Exception("Error al generar el PDF")

        # Guardar la ruta del archivo PDF en el modelo
        baja.archivo_anexo_a2 = pdf_path_a2
        baja.listopara_anexo_A3 = True
        
        baja.save()

        print(f"PDF generado con éxito y guardado en: {pdf_path_a2}")

        return redirect('bajas:list')  # Redirigir al listado de bajas después de crear el PDF

    except Exception as e:
        print(f"Error al generar el PDF: {e}")
        return render(request, 'bajas/error.html', {'mensaje': 'Error al generar el PDF'})
@login_required
def trabajar_anexoA3(request, id):
    baja = get_object_or_404(Bajas, pk=id)
    is_ledesma = request.user.username.lower() == 'ledesma'

    if request.method == 'POST':
        form = BajasForm(request.POST, request.FILES, instance=baja)
        if form.is_valid():  
            baja = form.save(commit=False)
            baja.informacion_anexo_a3_completa = True
            baja.save()
            return redirect('bajas:list')
    else:
        form = BajasForm(instance=baja)

    return render(request, 'bajas/editar_bajas.html', {'form': form, 'baja': baja, 'is_ledesma': is_ledesma})


@login_required
def crear_anexoA3(request, id):
    baja = get_object_or_404(Bajas, pk=id)  # Obtener la baja
    if not baja.informacion_anexo_a3_completa:
        # Si la información no ha sido completada, redirigir o mostrar un error
        return redirect('bajas:trabajar_anexoA3', id=id)

    # Generación del PDF
    print(f"Generando PDF para Anexo A3...")

    context = {
        'baja': baja,
        "logo_etecsa": request.build_absolute_uri(static('bajastecnicas/icons/etecsa_logo.jpeg'))
    }

    html_string_a3 = render_to_string('bajas/anexo_a3.html', context)

    pdf_path_a3 = f'anexos/anexo_{baja.id}_A3.pdf'
    try:
        with default_storage.open(pdf_path_a3, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(html_string_a3, dest=pdf_file)

            if pisa_status.err:
                raise Exception("Error al generar el PDF")

        # Guardar la ruta del archivo PDF en el modelo
        baja.archivo_anexo_a3 = pdf_path_a3
        
        
        baja.save()

        print(f"PDF generado con éxito y guardado en: {pdf_path_a3}")

        return redirect('bajas:list')  # Redirigir al listado de bajas después de crear el PDF

    except Exception as e:
        print(f"Error al generar el PDF: {e}")
        return render(request, 'bajas/error.html', {'mensaje': 'Error al generar el PDF'})
    
@login_required
def cargar_excel_inv(request):
    if request.method == 'POST':
        archivo = request.FILES.get('excel_file')

        if not archivo:
            messages.error(request, "No se seleccionó ningún archivo.")
            return redirect('bajas:cargar_excel_inv') 

        if archivo.name != 'inventario.xlsx':
            messages.warning(request, "El archivo debe llamarse exactamente 'inventario.xlsx'.")
            return redirect('bajas:cargar_excel_inv')  

        ruta_guardado = os.path.join(settings.MEDIA_ROOT, 'uploaded', 'inventario.xlsx')
        os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)

        try:
            with open(ruta_guardado, 'wb+') as destino:
                for chunk in archivo.chunks():
                    destino.write(chunk)

           
            messages.success(request, "El archivo fue cargado correctamente.")
            return redirect('bajas:cargar_excel_inv') 

        except Exception as e:
            # Si ocurre un error en el proceso de carga, mostramos el mensaje de error
            messages.error(request, f"Ocurrió un error al cargar el archivo: {str(e)}")
            return redirect('bajas:cargar_excel_inv')  

    return render(request, 'bajas/cargar_excel_inv.html')

