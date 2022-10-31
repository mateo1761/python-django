from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request, 'home.html')

def Platos(request):
    # Esta vista va a utilizar un formulario de django
    # Debo crear entonces un objeto de la clase FormularioPlatos

    formulario = FormularioPlatos()

    # Creamos un diccionario para enviar el formulario al HTML(TEMPLATE)
    
    data = {
        'formulario': formulario
    }

    return render(request, 'menuPlatos.html', data)

def Empleados(request):
    formulario = FormularioEmpleados()

    data = {
        'formulario': formulario
    }

    return render(request, 'empleados.html', data)

