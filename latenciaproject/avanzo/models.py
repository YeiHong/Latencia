from django.db import models


class Avanzo(models.Model):
    nombre = models.CharField(max_length = 255,null=True)
    empresas_vinculadas = models.ManyToOneRel

    def __str__(self):
        return '{}' .format(self.nombre)
