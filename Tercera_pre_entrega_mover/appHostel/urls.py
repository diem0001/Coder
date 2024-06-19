
from django.contrib import admin
from django.urls import path
from appHostel.views import *
from django.contrib.auth.views import LogoutView
urlpatterns =[
    
    path('cuartoFormulario/', agregar_cuarto, name='cuartoFormulario'),
    path('clienteFormulario/', agregar_cliente, name='clienteFormulario'),
    path('empleadoFormulario/', agregar_empleado, name='empleadoFormulario'),
    path("", inicio, name="inicio"),
    path("cuarto/", cuarto,name="cuartos"),
    path("cliente/", cliente,name="clientes"),
    path("empleado/", empleado,name="empleados"),
    path("listaEmpleados/", lista_empleados,name="listaEmpleados"),
    path("buscarPuesto/", buscar_puesto, name="buscarPuesto"),
    path("buscarEmpleados/", buscar, name="buscarEmpleados"),
    path("eliminarEmpleado/<int:id>", eliminarEmpleado, name="eliminarEmpleado"),
    path("EditaEmpleado/<int:id>", editar_empleado, name="EditaEmpleado"),
    path("Login/", login_view, name="Login"),
    path("registrar/", register, name="registrar"),
    path("logout/", LogoutView.as_view(template_name = "logout.html" ) , name="logout"),
    path("about/",about, name="about"),
    path("editarPerfil/",editar_perfil, name="editarPerfil"),
    path("agregarAvatar/",agregarAvatar, name="agregarAvatar"),
] 