from django.db import models

class Empleado(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    titulo = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50, default='Fisioterapeuta Aviar')

    def __str__(self):
        return f"{self.nombre} ({self.titulo})"
    
class AveDePresa(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"