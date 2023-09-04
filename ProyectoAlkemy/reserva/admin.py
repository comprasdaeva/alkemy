from django.contrib import admin
from reserva.models import *



class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ("id", "nombre", "apellido", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo",)
    
class ServicioAdmin(admin.ModelAdmin):
    model = Servicio
    list_display = ("id", "nombre", "descripcion", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)
    
class EmpleadoAdmin(admin.ModelAdmin):
    model = Empleado
    list_display = ("id", "nombre", "apellido", "numero_legajo", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo",)
    
class CoordinadorAdmin(admin.ModelAdmin):
    model = Coordinador
    list_display = ("id", "nombre", "apellido", "numero_documento", "fecha_alta", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo",)
    
class ReservaServicioAdmin(admin.ModelAdmin):
    model = ReservaServicio
    list_display = ("id", "fecha_creacion", "fecha_reserva", "cliente", "responsable", "empleado", "servicio", "precio")
    search_fields = ("responsable", "cliente", "empleado", "servicio")
    
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Coordinador, CoordinadorAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(ReservaServicio, ReservaServicioAdmin)
