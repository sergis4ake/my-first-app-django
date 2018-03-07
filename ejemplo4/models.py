from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.PositiveSmallIntegerField(default=25)
