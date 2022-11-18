from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

from web.models import Platos,Empleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request, 'home.html')

def Platos(request):
    # Rutina para consulta de datos
    platosConsultados=Platos.objects.all() #El metodo objects no lo esta recocnociendo
    # print (vars(platosConsultados=Platos.objects.all()))
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
                nombre_plato = datosLimpios['nombre'],
                fotografia = datosLimpios['fotografia'],
                precio = datosLimpios['precio'],
                tipo = datosLimpios['tipo'],
                descripcion = datosLimpios['descripcion']
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

def Empleados(request):
    formulario = FormularioEmpleados()

    data = {
        'formulario': formulario
    }

    return render(request, 'empleados.html', data)

