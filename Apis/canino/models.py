from django.db import models
from Apis.adopcion.models import Persona

# Create your models here.

class Sexo(models.Model):
    tipo = models.CharField(blank=False, max_length=15)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "sexo"
        verbose_name_plural = "sexo"


class Raza(models.Model):
    raza = models.CharField(max_length=100, default="desconocida")

    def __str__(self):
        return self.raza

    class Meta:
        verbose_name = "raza"
        verbose_name_plural = "razas"


class Vacuna(models.Model):
    nombre = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "vacuna"
        verbose_name_plural = "vacunas"


class Perro(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField(blank=True, null=True)
    rescate = models.DateField()
    sexo = models.ForeignKey(Sexo, null=True, blank=False)
    raza = models.ForeignKey(Raza, blank=True, null=True)
    vacuna = models.ManyToManyField(Vacuna, blank=True)
    adoptante = models.ForeignKey(Persona, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.raza)

    class Meta:
        verbose_name = "perro"
        verbose_name_plural = "perros"
