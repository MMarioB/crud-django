from django.db import models
from django.urls import reverse

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    identificador = models.CharField(max_length=200, null=False)
    direccion = models.CharField(max_length=200, null=True)
    departamento = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('estudiante_editar', kwargs={'pk': self.pk})