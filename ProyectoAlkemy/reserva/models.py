from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=50)
    numero_legajo = models.IntegerField(verbose_name="Numero de legajo", unique=True)
    activo = models.BooleanField(verbose_name="Activo",default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Coordinador(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=50)
    numero_documento = models.IntegerField(verbose_name="Numero de documento", unique=True)
    fecha_alta = models.DateTimeField(verbose_name="Fecha de alta",auto_now_add=True)
    activo = models.BooleanField(verbose_name="Activo",default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=50)
    activo = models.BooleanField(verbose_name="Activo",default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Servicio(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=50)
    precio = models.IntegerField(verbose_name="Precio")
    activo = models.BooleanField(verbose_name="Activo", default=True)
    
    def __str__(self):
        return f"{self.nombre}"

class ReservaServicio(models.Model):
    fecha_creacion = models.DateTimeField(verbose_name="Fecha de creacion",auto_now_add=True)
    fecha_reserva = models.DateTimeField(verbose_name="Fecha de reserva")
    cliente = models.ForeignKey(Cliente,verbose_name="Cliente",on_delete=models.CASCADE,related_name="cliente")
    responsable = models.ForeignKey(Coordinador,verbose_name="Coordinador",on_delete=models.CASCADE,related_name="coordinador")
    empleado = models.ForeignKey(Empleado,verbose_name="Empleado",on_delete=models.CASCADE,related_name="empleado")
    servicio = models.ForeignKey(Servicio,verbose_name="Servicio",on_delete=models.CASCADE,related_name="servicio")
    precio = models.IntegerField(verbose_name="Precio")
    
    def get_fecha_creacion_formateada(self):
        return self.fecha_creacion.strftime("%d/%m/%Y %H:%M")
    
    def get_fecha_reserva_formateada(self):
        return self.fecha_reserva.strftime("%d/%m/%Y %H:%M")
    
    def __str__(self):
        return f"{self.cliente} {self.responsable} {self.empleado} {self.servicio}"
