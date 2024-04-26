from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=150)
    no_calle = models.CharField(max_length=150)
    pais = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Domicilio {self.id} {self.calle} {self.no_calle} {self.pais}"

class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.CharField(max_length=120)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"Persona {self.id} {self.nombre} {self.apellido} {self.email}"
    