from django.db import models

# Create your models here.

#Modelo de Rescatado
class Raza(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Estado(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Rescatado(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    fotografia = models.CharField(max_length = 200, default='.jpg')
    raza = models.ForeignKey(Raza, default=1, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)



