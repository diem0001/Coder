
from django.contrib import admin
from django.urls import path
from appHostel.views import agregar_cliente,agregar_cuarto,agregar_empleado,inicio,cliente,cuarto,buscar_puesto,empleado,lista_empleados,buscar

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

] 