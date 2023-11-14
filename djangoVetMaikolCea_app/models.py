from django.db import models

# Create your models here.

class Paciente(models.Model):
    ID              = models.CharField(max_length=10)
    nombre          = models.CharField(max_length=50)
    microchips      = models.CharField(max_length=12)
    fecha_atencion  = models.CharField(max_length=50)
    motivo          = models.CharField(max_length=50)
    diagnostico     = models.CharField(max_length=50)


class detalleTratamiento(models.Model):
    nombre = models.CharField(max_length=50)
    observacion = models.CharField(max_length=12)
    valor       = models.CharField(max_length=50)

class Tratamientos(models.Model):
    pacientes   = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tratamiento = models.ManyToManyField(Tratamiento)
    
