from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
