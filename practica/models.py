from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.PositiveSmallIntegerField(default=25)

class Actividad(models.Model):
    nombre = models.CharField(max_length=20)
    peso = models.FloatField(default=0.0)

class InformeActividad(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    nota = models.FloatField(default=0.0)
