# -*- encoding: utf-8 -*-
from django.views.generic import View
import datetime
import time
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Conexiones
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required # Forma para impedir el acceso al sistema
import os
import csv
#=====================================================================================
# Llamado de rest_framework para la api de Conexioness
#=====================================================================================
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from django import http
from django.http import Http404
from django.db import connection, transaction  # Cursor de django
from apps.cantidad_usuario.formato_reportes import reporte_expo
#=====================================================================================
#               # Metodo para el registro de cantidad de usuarios wifi
#=====================================================================================

# def cantidad_save(request):
#     
#     
#     if request.POST.get('accion') == "depurar_data":
#         
#         cursor = connection.cursor()
#         query = "TRUNCATE reportes_tabladinamica RESTART IDENTITY"
#         cursor.execute(query,[])
#         
#         return HttpResponse('depurar')
#     
#     if request.POST.get('accion') == "guardar":
#         
#         # ###print "Agrego
#         cantidad = request.POST['cantidad']
#         aumento = request.POST['aumento']
#         hora = time.strftime("%I:%M %p")
#         codigo = Conexiones.objects.count()
#         codigo = str(codigo + 1).zfill(4)
#         
#         # =========================================
#         #                  Calculo
#         # =========================================
#         subida = int(cantidad) * 24
#         bajada = int(cantidad) * 56
#         # =========================================
#         
#         obj = Conexiones(
#             cantidad = cantidad,
#             aumento = aumento,
#             hora = hora,
#             codigo = codigo,
#             subida_usu = subida,
#             bajada_usu = bajada,
#         )
#         obj.save()
#         return HttpResponse('add')
# 
#     ctx = {'cantidad_usu':Conexiones.objects.all().order_by('id'),}
#     return render_to_response('cantidad_usuario/procesar.html', ctx, context_instance=RequestContext(request))
# 
# 
# class ExpoReporte(View):
#     
#     model = Conexiones
#     
#     def get(self, request, *args, **kwargs):
#         
#         desde = kwargs.get('from_date', None)
#         hasta = kwargs.get('to_date', None)
#         
#         cursor = connection.cursor()
#         sql_det = "SELECT cantidad, subida_usu, bajada_usu, aumento "
#         sql_det += " FROM cantidad_usuario_cantidadusuario "
#         sql_det += " ORDER BY id "
#         cursor.execute(sql_det)
#         row = dictfetchall(cursor)
# 
#         nombre, archivo = reporte_expo.reporte_expo(desde,hasta)
#         response = HttpResponse(archivo.read(), content_type='application/pdf')
#         response['Content-Disposition'] = 'inline; filename="'+str(nombre)
#         
#         return response
#         

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]