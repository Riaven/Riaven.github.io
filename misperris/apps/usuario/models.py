from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Modelo tipo de vivienda
class TipoVivienda(models.Model):
    nombre = models.CharField(max_length=50)

    def __srt__(self):
        return '{}'.format(self.nombre)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 100)
    correo = models.EmailField()
    run = models.CharField(max_length = 10)
    fecha_nac = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length = 14)
    region = models.CharField(max_length = 50)
    comuna = models.CharField(max_length = 50)
    tipo_vivienda = models.ForeignKey(TipoVivienda, default=1, on_delete=models.CASCADE)
    
    def __srt__(self):
        return '{}'.format(self.nombre)
        