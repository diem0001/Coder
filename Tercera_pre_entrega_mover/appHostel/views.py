from django.http import HttpResponse
from django.shortcuts import render
from appHostel.models import Cuarto,Cliente,Empleado,Avatar
from .forms import CuartoFormulario,ClienteFormulario,EmpleadoFormulario,UserEditForm,AvatarFormulario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='/appHostel/Login')
def agregar_cuarto(req):
    if req.method == "POST":

        miFormulario = CuartoFormulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            cuarto = Cuarto(nombre = informacion["nombre"], numero = informacion["numero"],capacidad = informacion["capacidad"])

            cuarto.save()

            return render (req,"inicio.html",{"mensaje":"Los datos se cargaron correctamente"})
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})
    else:
        miFormulario = CuartoFormulario()

        return render(req,"cuartoFormulario.html",{"miFormulario": miFormulario})

    
    
    

@staff_member_required(login_url='/appHostel/Login')
def agregar_cliente(req):

    if req.method == "POST":

        miFormulario = ClienteFormulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            cliente = Cliente(nombre = informacion["nombre"], napellido = informacion["apellido"],edad = informacion["edad"],nacionalidad = informacion["nacionalidad"])

            cliente.save()

            return render (req,"inicio.html",{"mensaje":"Los datos se cargaron correctamente"})
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})

    else:
        miFormulario = ClienteFormulario()

        return render(req,"clienteFormulario.html",{"miFormulario": miFormulario})
    

@staff_member_required(login_url='/appHostel/Login')
def agregar_empleado(req):
   
    if req.method == "POST":

        miFormulario = EmpleadoFormulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            empleado = Empleado(nombre = informacion["nombre"], apellido = informacion["apellido"],puesto = informacion["puesto"])

            empleado.save()

            return render (req,"inicio.html",{"mensaje":"Los datos se cargaron correctamente"})
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})

    else:
        miFormulario = EmpleadoFormulario()

        return render(req,"empleadoFormulario.html",{"miFormulario": miFormulario})


def inicio(req):
    avatar_url = None
    if req.user.is_authenticated:
        avatar = Avatar.objects.filter(user=req.user).first()
        if avatar:
            avatar_url = avatar.imagen.url
    return render(req, 'inicio.html', {'avatar_url': avatar_url})

    

    


def cuarto(req):

    return render(req,"cuarto.html", {})

def empleado(req):

    return render(req,"empleado.html", {})

def cliente(req):

    return render(req,"cliente.html", {})


@staff_member_required(login_url='/appHostel/Login')
def lista_empleados(req):

    mis_empleados = Empleado.objects.all()

    return render(req,"listaEmpleados.html",{"empleados": mis_empleados})

def eliminarEmpleado(req,id):

    if req.method == 'POST':


        empleado = Empleado.objects.get(id=id)
        empleado.delete()

        mis_empleados = Empleado.objects.all()

    return render(req,"listaEmpleados.html",{"empleados": mis_empleados})


def editar_empleado(req,id):

    if req.method == "POST":

        miFormulario = EmpleadoFormulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            empleado = Empleado.objects.get(id = id)

            empleado.nombre = informacion["nombre"]
            empleado.apellido = informacion["apellido"]
            empleado.puesto = informacion["puesto"]
           
            empleado.save()

            return render (req,"inicio.html",{"mensaje":"Empleado actualizado con exito"})
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})

    else:
        empleado = Empleado.objects.get(id = id)

        miFormulario = EmpleadoFormulario(initial={
          "nombre": empleado.nombre,
          "apellido": empleado.apellido,
          "puesto": empleado.puesto,  
        })

        return render(req,"editarEmpleado.html",{"miFormulario": miFormulario, "id":  empleado.id})

@staff_member_required(login_url='/appHostel/Login')
def buscar_puesto(req):
    return render(req, "buscarpuesto.html", {})

def buscar(req):
    if "nombre" in req.GET and req.GET["nombre"]:
        nombre = req.GET["nombre"]
        empleados = Empleado.objects.filter(nombre__icontains=nombre)
        
        if empleados.exists():
            return render(req, "resultadoBusqueda.html", {"empleados": empleados, "nombre": nombre})
        else:
            return render(req, "inicio.html", {"mensaje": "No se encontraron empleados con ese nombre"})
    else:
        return render(req, "inicio.html", {"mensaje": "Datos inválidos"})
    

def login_view(req):

    if req.method == "POST":

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario = informacion["username"]
            psw = informacion["password"]

            user = authenticate(username = usuario, password = psw)

            if user:
                login(req, user)
                return render (req,"inicio.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                return render (req,"inicio.html",{"mensaje":"Datos erroneos"})
            
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})

    else:
        miFormulario = AuthenticationForm()

        return render(req,"Login.html",{"miFormulario": miFormulario})
    

def register(req):

    if req.method == "POST":

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario = informacion["username"]
            miFormulario.save()
            

            return render (req,"inicio.html",{"mensaje":f"Usuario {usuario} Creado con exito!"})
            
            
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})
   
    else:
        miFormulario = UserCreationForm()

        return render(req,"registro.html",{"miFormulario": miFormulario}) 
    
def about(req):
    return render(req,"about.html")


#----------------------------------------------------------------------------------------------
@login_required
def editar_perfil(req):

    usuario = req.user

    if req.method == "POST":

        miFormulario = UserEditForm(req.POST, instance =req.user)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"])

            usuario.save()

            return render (req,"inicio.html",{"mensaje":" Datos actualizado con exito"})
        else:
            return render (req,"editarPerfil.html",{"miFormulario": miFormulario})

    else:
        

        miFormulario = UserEditForm(instance=req.user)

        return render(req,"editarPerfil.html",{"miFormulario": miFormulario})


def agregarAvatar(req):

    if req.method == "POST":

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            
            created = Avatar.objects.update_or_create(
                user=req.user,
                defaults={'imagen': informacion["imagen"]}
            )
            mensaje = "Avatar cargado con éxito" if created else "Avatar actualizado con éxito"
            return render(req, "inicio.html", {"mensaje": mensaje})
        else:
            return render(req, "inicio.html", {"mensaje": "Datos inválidos"})
    else:
        

        miFormulario = AvatarFormulario()

        return render(req,"agregarAvatar.html",{"miFormulario": miFormulario})