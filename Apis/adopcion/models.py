from django.db import models

# Create your models here.

class Persona(models.Model):
    # TODO: Define fields here
    nombre = models.CharField(blank=True, max_length=100)
    apellidos = models.CharField(blank=True, max_length=150)
    edad = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    domicilio = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Solicitud(models.Model):
    # TODO: Define fields here
    persona = models.ForeignKey(Persona, null=True, blank=True)
    numero_caninos = models.IntegerField(blank=True, null=True)
    razon = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

    def __str__(self):
        salida = 'solicitud'
        if self.persona:
            return '{}'.format(self.persona)
        else:
            return '{} {}'.format(salida, self.id)
