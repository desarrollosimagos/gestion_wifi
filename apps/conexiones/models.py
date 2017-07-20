
# -*- encoding: utf-8 -*-
from django.db import models


# Esta es mi CLASE.


class Conexiones(models.Model):
    """
	Esta es la Clase que define todo lo referente a la cantidad de usuarios conectados a la wifi
        Registrar, visualiza las tendencias de conexion

	:param CharField cod_estado: campo donde se registra el c?digo del estado.
    """
    mac = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True, auto_now=False, null=True)
    hora = models.CharField(max_length=10, null=True, blank=True)  

    def __unicode__(self):
        return self.mac