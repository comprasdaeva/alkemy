from rest_framework import serializers
from .models import Empleado,ReservaServicio


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Empleado
        fields = ["id","nombre","apellido","numero_legajo","activo"]
    
class ReservasServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaServicio
        fields = '__all__'