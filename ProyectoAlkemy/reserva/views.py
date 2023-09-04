from django.shortcuts import render
from .models import Empleado, Cliente, Coordinador, Servicio, ReservaServicio
from django.shortcuts import get_object_or_404,redirect
from datetime import datetime
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, "reserva/home.html")

def registrar_empleado(request):

    if request.method == "POST":        
        try:
            Empleado.objects.create(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            numero_legajo = request.POST["numero_legajo"],
            );
            return redirect('listado_empleados')
        except IntegrityError:

            return redirect('listado_empleados')
            
    return render(request, 'reserva/registrar_empleado.html')
    
def activar_empleado(request,id_empleado):
  
    empleado=Empleado.objects.get(id=id_empleado);
    empleado.activo=True;
    empleado.save();

    return redirect('listado_empleados')

def listado_empleados(request):
    empleados = Empleado.objects.all()
    context = {
        "empleados": empleados
    }
    return render(request, "reserva/listar_empleados.html", context)

def modificar_empleado(request, id_empleado):    
    empleado=Empleado.objects.get(id=id_empleado)    
    context = {
        "empleado": empleado
    }
    if request.method == "POST":  
        try:
            empleado.nombre = request.POST["nombre"]
            empleado.apellido = request.POST["apellido"]
            empleado.numero_legajo = request.POST["numero_legajo"]
            empleado.save()
            return redirect('listado_empleados')
       
        except IntegrityError:

            return redirect('listado_empleados')
          
    return render(request, "reserva/modificar_empleado.html", context)

def desactivar_empleado(request,id_empleado):
      
    empleado=Empleado.objects.get(id=id_empleado)
    empleado.activo=False
    empleado.save()

    return redirect('listado_empleados')

def listado_clientes(request):
    clientes = Cliente.objects.all()
    context = {
        "clientes": clientes
    }
    return render(request, "reserva/listar_clientes.html", context)

def registrar_cliente(request):

    if request.POST:

        Cliente.objects.create(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
        )
        return redirect('listado_clientes')
        
    return render(request,'reserva/registrar_cliente.html')

def registrar_coordinador(request):

    if request.method == "POST":
        try:    
            Coordinador.objects.create(
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                numero_documento = request.POST["numero_documento"]
            )
            return redirect('listado_coordinadores')
        except IntegrityError:
           return redirect('listado_coordinadores')
            
        
    return render(request,'reserva/registrar_coordinador.html')

def modificar_coordinador(request,id_coordinador):

    coordinador = get_object_or_404(Coordinador, id=id_coordinador)
    if request.method == "POST": 
        try:
            
            coordinador.nombre = request.POST["nombre"]
            coordinador.apellido = request.POST["apellido"]
            coordinador.numero_documento = request.POST["numero_documento"]
            coordinador.save()
            return redirect('listado_coordinadores')
        except IntegrityError:
            return redirect('listado_coordinadores')
    
    return render(request,'reserva/modificar_coordinador.html',{"coordinador": coordinador})

def activar_coordinador(request,id_coordinador):
      
    coordinador = Coordinador.objects.get(id=id_coordinador)
    coordinador.activo = True
    coordinador.save()
    return redirect('listado_coordinadores')

def desactivar_coordinador(request,id_coordinador):
      
    coordinador = Coordinador.objects.get(id=id_coordinador)
    coordinador.activo = False
    coordinador.save()
    return redirect('listado_coordinadores')

def desactivar_cliente(request,id_cliente):

    cliente = get_object_or_404(Cliente,id=id_cliente)
    if cliente.activo:
       cliente.activo=False
       cliente.save()
    
    return redirect('listado_clientes')

def activar_cliente(request,id_cliente):

    cliente = get_object_or_404(Cliente,id=id_cliente)
    if not cliente.activo:
       cliente.activo=True
       cliente.save()

    return redirect('listado_clientes')

def modificar_cliente(request,id_cliente):

    cliente = get_object_or_404(Cliente, id=id_cliente);
    if request.method == "POST":
        cliente.nombre = request.POST["nombre"]
        cliente.apellido = request.POST["apellido"]
        cliente.save();
        return redirect('listado_clientes')        
    
    return render(request,'reserva/modificar_cliente.html',{"cliente":cliente})

def listado_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    context = {
        "coordinadores": coordinadores
    }
    return render(request, "reserva/listar_coordinador.html", context)


def registrar_servicio(request):

    if request.POST:

        Servicio.objects.create(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            precio = request.POST["precio"],                 
        )
        return redirect('listado_servicios')
        
    return render(request,'reserva/registrar_servicio.html')

def registrar_reserva_de_servicio(request):

    clientes=Cliente.objects.filter(activo=True)
    responsables=Coordinador.objects.filter(activo=True)
    empleados=Empleado.objects.filter(activo=True)
    servicios=Servicio.objects.filter(activo=True)
    contexto={
        "clientes":clientes,
        "responsables":responsables,
        "empleados": empleados,
        "servicios": servicios,
        "fecha_actual": get_fecha_hora_actual()
    }
    if request.method == "POST":
        ReservaServicio.objects.create(
            fecha_reserva = request.POST["fecha_reserva"],
            cliente_id = request.POST["cliente"],
            responsable_id = request.POST["responsable"],
            empleado_id = request.POST["empleado"],
            servicio_id = request.POST["opcion"],
            precio = request.POST["precio"]
        )
        return redirect('listado_reservas_de_servicios')
    
    return render(request, "reserva/registrar_reserva_de_servicio.html",contexto)

def modificar_reserva_de_servicio(request,id_reserva_servicio):
    
    reserva_servicio = get_object_or_404(ReservaServicio,id=id_reserva_servicio)
    clientes = Cliente.objects.filter(activo=True)
    responsables = Coordinador.objects.filter(activo=True)
    empleados = Empleado.objects.filter(activo=True)
    servicios = Servicio.objects.filter(activo=True)
    contexto = {
        "reserva_servicio": reserva_servicio,
        "clientes": clientes,
        "responsables": responsables,
        "empleados": empleados,
        "servicios": servicios,
        "fecha_actual": get_fecha_hora_actual()
    }
    if request.method == "POST":
        reserva_servicio.fecha_reserva = request.POST["fecha_reserva"]
        reserva_servicio.cliente_id = request.POST["cliente"]
        reserva_servicio.responsable_id = request.POST["responsable"]
        reserva_servicio.empleado_id = request.POST["empleado"]
        reserva_servicio.servicio_id = request.POST["opcion"]
        reserva_servicio.precio = request.POST["precio"]
        
        reserva_servicio.save();
        return redirect('listado_reservas_de_servicios')

    return render(request,"reserva/modificar_reserva_de_servicio.html",contexto)


def eliminar_reserva_de_servicio(request,id_reserva_servicio):
    
    reserva_servicio = get_object_or_404(ReservaServicio,id=id_reserva_servicio)
    reserva_servicio.delete()
    
    return redirect('listado_reservas_de_servicios')

def listado_reservas_de_servicios(request):

    reservas = ReservaServicio.objects.all();

    return render(request,"reserva/listar_reservas_de_servicios.html",{"reservas":reservas})

def modificar_servicio(request, id_servicio):    
    
    servicio=Servicio.objects.get(id=id_servicio)    
    
    context = {
        "servicio": servicio
    }
    if request.POST:        
        nombre = request.POST["nombre"],
        descripcion = request.POST["descripcion"],
        precio = request.POST["precio"],
        
        servicio.nombre = nombre[0]
        servicio.descripcion = descripcion[0]
        servicio.precio = int(precio[0])
        servicio.save()
        return redirect('listado_servicios')
          
    return render(request, "reserva/modificar_servicio.html", context)

def desactivar_servicio(request,id_servicio):

    servicio = get_object_or_404(Servicio,id=id_servicio)
    if servicio.activo:
       servicio.activo=False
       servicio.save()
    
    return redirect('listado_servicios')

def activar_servicio(request,id_servicio):

    servicio = get_object_or_404(Servicio,id=id_servicio)
    if not servicio.activo:
       servicio.activo=True
       servicio.save()

    return redirect('listado_servicios')

def listado_servicios(request):
    servicios = Servicio.objects.all()
    context = {
        "servicios": servicios
    }
    return render(request, "reserva/listar_servicios.html", context)

def get_fecha_hora_actual():
    
    fecha_actual = datetime.now()
    fecha_actual_medianoche=datetime(fecha_actual.year,fecha_actual.month,fecha_actual.day);
    return fecha_actual_medianoche.strftime('%Y-%m-%d %H:%M:%S')
