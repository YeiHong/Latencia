from django.db import models
from avanzo.models import Avanzo

class EmpresaVinculada(models.Model):
    avanzo = models.ForeignKey(Avanzo, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=255,null=True)
    razon_social = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s' % (self.nombre, self.nit)
