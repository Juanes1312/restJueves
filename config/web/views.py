from django.shortcuts import render


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

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
    }
    return render(request,'empleados.html')

