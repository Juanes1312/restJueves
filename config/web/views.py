from django.shortcuts import render
from django.shortcuts import redirect


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos


from web.models import Platos
from web.models import Empleados

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def MenuPlatos(request):

    platosConsultados=Platos.objects.all()

    formulario=FormularioEdicionPlatos()

    diccionarioEnvio={
        'platos':platosConsultados,
        'formulario':formulario
    }

    return render(request, 'menuPlatos.html', diccionarioEnvio)

def EditarPlatos(request,id):
    # resivir los datos del formulario y editar el plato
    if request.method=='POST':
        datosDelFormulario=FormularioEdicionPlatos(request.POST)
        if datosDelFormulario.is_valid():
            datosPlato=datosDelFormulario.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(precio=datosPlato["precioPlato"])
                print("exito guardando")

            except Exception as error:
                print("error ",error)

    return render(request, 'menuPlatos.html')


def VistaPlatos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario,
        'bandera':False
    }

    #PREGUNTAMOS SI EXISTE ALGUNA PETICION DE TIPO POST ASOCIADA A LA VISTA
    if request.method=='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            #creamos un objeto de tipo modelo plato 
            platoNuevo=Platos(
                nombre=datosPlato["nombrePlato"],
                descripcion=datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio=datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"]
            )
            #intentamos llevar el objeto plato nuevo a la BD
            try:
                platoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("exito guardando")

            except Exception as error:
                datosParaTemplate["bandera"]=False
                print("error ",error)

    return render(request,'platos.html',datosParaTemplate)


def VistaEmpleados(request):

    formulario=FormularioEmpleados()
    datosParaTemplate={
        'formularioRegistro':formulario,
        'bandera':False
    }

    #PREGUNTAMOS SI EXISTE ALGUNA PETICION DE TIPO POST ASOCIADA A LA VISTA
    if request.method=='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioEmpleados(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosEmpleado=datosDelFormulario.cleaned_data
            #creamos un objeto de tipo modelo plato 
            empleadoNuevo=Empleados(
                nombres=datosEmpleado["nombres"],
                apellidos=datosEmpleado["apellidos"],
                foto=datosEmpleado["foto"],
                cargo=datosEmpleado["cargo"],
                salario=datosEmpleado["salario"],
                contacto=datosEmpleado["contacto"]
            )
            #intentamos llevar el objeto Empleado nuevo a la BD
            try:
                empleadoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("exito guardando")

            except Exception as error:
                datosParaTemplate["bandera"]=False
                print("error ",error)

    return render(request,'empleados.html', datosParaTemplate)

