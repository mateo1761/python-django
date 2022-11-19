from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

from web.models import Platos
from web.models import Empleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request, 'home.html')

def PlatosVista(request):
    # Rutina para consulta de datos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)

    # Esta vista va a utilizar un formulario de django
    # Debo crear entonces un objeto de la clase FormularioPlatos

    formulario = FormularioPlatos()

    # Creamos un diccionario para enviar el formulario al HTML(TEMPLATE)
    
    data = {
        'formulario': formulario,
        'bandera':False,
        'platos':platosConsultados
    }

    #RECIBIMOS LOS DATOS DEL FORMULARIO 

    if request.method == 'POST':
        datosForms = FormularioPlatos(request.POST)
        if datosForms.is_valid():
            datosLimpios = datosForms.cleaned_data
            print(datosLimpios)
            #Construir un diccionario de envio de datos gacia la BD

            platoNuevo = Platos(
                nombre = datosLimpios['nombre'],
                descripcion = datosLimpios['descripcion'],
                imagen = datosLimpios['fotografia'],
                precio = datosLimpios['precio'],
                tipo = datosLimpios['tipo'],
            )
            #Intentare llevar mis datos a la BD

            try:
                platoNuevo.save()
                data['bandera']=True
                print('Exito guardando datos')
            except Exception as error:
                print('Error al guardar los datos: ', error)
                data['bandera']=False


    return render(request, 'menuPlatos.html', data)

def EmpleadosVista(request):
    empleadosConsultados = Empleados.objects.all()
    print(empleadosConsultados)

    formulario = FormularioEmpleados()

    data = {
        'formulario': formulario,
        'bandera' : False,
        'empleados' : empleadosConsultados
    }

    if request.method == 'POST':
        datosForms = FormularioEmpleados(request.POST)
        if datosForms.is_valid():
            datosLimpios = datosForms.cleaned_data
            print(datosLimpios)
            #Construir un diccionario de envio de datos gacia la BD

            empleadoNuevo = Empleados(
                nombre = datosLimpios['nombre'],
                apellido = datosLimpios['apellido'],
                imagen = datosLimpios['fotografia'],
                cargo = datosLimpios['cargo'],
                salario = datosLimpios['Salario'],
                contacto = datosLimpios['contacto'],
            )
            #Intentare llevar mis datos a la BD

            try:
                empleadoNuevo.save()
                data['bandera']=True
                print('Exito guardando datos')
            except Exception as error:
                print('Error al guardar los datos: ', error)
                data['bandera']=False

    return render(request, 'empleados.html', data)

