from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

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