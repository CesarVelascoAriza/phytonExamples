from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.CharField(max_length=120)