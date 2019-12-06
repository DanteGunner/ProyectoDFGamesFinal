from django.db import models

# Create your models here.

class Compania(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Juego(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    anio_lanzamiento = models.IntegerField(verbose_name='año lanzamiento')
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
