from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest,Http404
from reserva.models import Servicio,Coordinador,Cliente,Empleado,ReservaServicio
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
#Django rest
from django.views.decorators.csrf import csrf_exempt
from reserva.serializers import EmpleadoSerializer,ReservasServicioSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def servicios_listado(request):
    servicios = Servicio.objects.values('id','nombre','precio')
    
    return JsonResponse(list(servicios),safe=False);

def servicio_por_id(request,id_servicio):
    try:
        
        servicio = Servicio.objects.get(id=id_servicio)
        servicio_json = { 
            'id': servicio.id,
            'nombre': servicio.nombre,
            'precio': servicio.precio
        }
        return JsonResponse(servicio_json, safe=False)
    except ObjectDoesNotExist:

        servicio_json = []
        respuesta = JsonResponse(servicio_json, safe=False)
        respuesta.status_code=404
        #JsonResponse.status_code=400;
        return respuesta
        #return HttpResponse(content=servicio_json, content_type="status=status.HTTP_200_OK")
    
    

def coordinadores_listado(request):
    coordinadores=Coordinador.objects.values();

    return JsonResponse(list(coordinadores),safe=False);
    
def clientes_listado(request):
    clientes=Cliente.objects.values();

    return JsonResponse(list(clientes),safe=False)

""" def empleados_listado(request):
    empleados=Empleado.objects.values();

    return JsonResponse(list(empleados),safe=False) """

class EmpleadosAPI(APIView):

    def get_empleado(self,id):
        try:
            empleado= Empleado.objects.get(id=id);
            return empleado;
        except Empleado.DoesNotExist:
            raise Http404    

    def get_lista_empleados(self,request):
        empleados = EmpleadoSerializer(Empleado.objects.all(),many=True);
        return Response(empleados.data)
    
    def get_empleado_por_id(self,request,id_empleado):
        try:
            empleado = EmpleadoSerializer(self.get_empleado(id_empleado))
            return Response(empleado.data);
        except Http404:
            return Response({"mensaje":f"No se encontro el empleado {id_empleado}"},status=404)

    def get(self,request,id_empleado=None):
        
        if id_empleado is None:
            return self.get_lista_empleados(request)
        else:
            return self.get_empleado_por_id(request, id_empleado)

    def delete(self,request,id_empleado):

        try:
            empleado=self.get_empleado(id_empleado)   
            empleado.delete()
            return Response(status=204)
        except Http404:
            return Response(data={"mensaje":f"No se encontro empleado con id {id_empleado}"},status=404)
        
    def post(self,request):

        empleado=EmpleadoSerializer(data=request.data);
        if empleado.is_valid(raise_exception=True):
            empleado.save()

        return Response({"mensaje":"Empleado creado correctamente"});          

    def put(self,request,id_empleado):
        try:
            empleado=EmpleadoSerializer(self.get_empleado(id_empleado),data=request.data);
            if empleado.is_valid(raise_exception=True):
                empleado.save()
                return Response(status=204)
        except Http404:
            return Response({"mensaje":"Empleado no encontrado"},status=404)
        
class ReservaAPI(APIView):

    def get(self,request):
        reserva=ReservasServicioSerializer(ReservaServicio.objects.all(),many=True);

        return Response(reserva.data)