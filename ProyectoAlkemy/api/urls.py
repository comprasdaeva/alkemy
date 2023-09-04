from django.urls import path, include
from . import views

urlpatterns = [
    path('servicios/',views.servicios_listado,name="servicios_listado"),
    path('servicios/<int:id_servicio>', views.servicio_por_id,name="servicio_por_id"),
    path('coordinadores/', views.coordinadores_listado,name="coordinadores_listado"),
    path('clientes/',views.clientes_listado,name="clientes_listado"),
    path('empleados/', views.EmpleadosAPI.as_view(), name="api_empleados_listado"),
    path('empleados/eliminar/<int:id_empleado>', views.EmpleadosAPI.as_view(), name="api_eliminar_empleado"),
    path('empleados/<int:id_empleado>',views.EmpleadosAPI.as_view(),name="api_empleado_id"),
    path('empleados/crear',views.EmpleadosAPI.as_view(),name="api_crear_empleado"),
    path('empleados/modificar/<int:id_empleado>',views.EmpleadosAPI.as_view(),name="api_modificar_empleado"),
    path('reserva/', views.ReservaAPI.as_view(), name="api_reserva_listado")
]
