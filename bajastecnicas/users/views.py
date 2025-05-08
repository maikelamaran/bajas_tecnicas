from django.shortcuts import redirect, render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def register_view(request):
    if request.method == "POST":#el form ha sido submited
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bajas:list")#aqui si el form is valid y todo salió bien
    else:#caso get request, simplemente envio el formulario vacio
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):  # Cambiamos el nombre de la función aquí
    if request.method == "POST":  # el form ha sido submited
        form = AuthenticationForm(data=request.POST)  # authenticationform espera que le pases el argument data
        if form.is_valid():            
            login(request, form.get_user())  # usamos el login renombrado
            if 'next' in request.POST:#quiero que si hay next vaya a donde quiera que next me diga para ir
                return redirect(request.POST.get('next'))
            return redirect("bajas:list")  # aqui si el form is valid y todo salió bien      
            
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("bajas:list")
    # Si la solicitud es GET, redirige a la página principal
    return redirect("bajas:list")

@login_required
def manage_roles_view(request):
    # Solo permitir si es superuser o tiene el permiso explícito
    if not (request.user.is_superuser or request.user.has_perm("users.administrador_roles")):
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    users = User.objects.all()
    permissions = Permission.objects.filter(codename__in=[
        "administrador_roles",
        "aprobar_anexo_a", "aprobar_anexo_a1", "aprobar_anexo_a2", "aprobar_anexo_a3",
        "llenar_anexo_a", "llenar_anexo_a1", "llenar_anexo_a2", "llenar_anexo_a3",
        "crear_anexo_a", "crear_anexo_a1", "crear_anexo_a2", "crear_anexo_a3",
    ])

    if request.method == "POST":
        for user in users:
            for perm in permissions:
                checkbox_name = f"user_{user.id}_perm_{perm.codename}"
                has_checkbox = checkbox_name in request.POST
                has_permission = user.user_permissions.filter(pk=perm.pk).exists()

                if has_checkbox and not has_permission:
                    user.user_permissions.add(perm)
                elif not has_checkbox and has_permission:
                    user.user_permissions.remove(perm)
        return redirect("users:manage_roles")

    return render(request, "users/manage_roles.html", {
        "users": users,
        "permissions": permissions,
    })