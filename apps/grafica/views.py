# -*- encoding: utf-8 -*-
import datetime
import time
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required # Forma para impedir el acceso al sistema
import os
import csv
from apps.grafica.models import TablaDinamica
#=====================================================================================
# Llamado de rest_framework para la api de CantidadUsuarios
#=====================================================================================
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from django import http
from django.http import Http404
import json
from django.db import connection, transaction  # Cursor de django
import random
#=====================================================================================
#               # Metodo para el registro de cantidad de usuarios wifi
#=====================================================================================

def mostrar_totales(request):
    
    accion = request.POST.get('accion')
    
    
    if accion == "total_general":
        response_data = []
        cursor = connection.cursor()
        sql_aum = "SELECT SUM(aumento) AS aumento FROM cantidad_usuario_cantidadusuario"
        cursor.execute(sql_aum,[])
        
        queryset = dictfetchall(cursor)
        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1
        data = json.dumps(response_data)
        return HttpResponse(data, content_type='application/json')
    
    if accion == "cantidad_actual":
        response_data = []
        cursor = connection.cursor()
        sql_can = "SELECT cantidad FROM cantidad_usuario_cantidadusuario ORDER BY codigo DESC limit 1"
        cursor.execute(sql_can,[])
        
        queryset = dictfetchall(cursor)
        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1
        data = json.dumps(response_data)
        return HttpResponse(data, content_type='application/json')
        
    
    # Proceso para reflejar la cantidad maxima
    if accion == "mostrar_cantidad":
        response_data = []
        cursor = connection.cursor()
        sql_can = "SELECT cantidad FROM cantidad_usuario_cantidadusuario ORDER BY cantidad DESC limit 1"
        cursor.execute(sql_can,[])
        
        queryset = dictfetchall(cursor)
        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1
        data = json.dumps(response_data)
        return HttpResponse(data, content_type='application/json')
    
    # Proceso para reflejar la cantidad total de tasa de subida y bajada de usuarios conectados
    if accion == "mostrar_total_s_b":
        
        response_data = []
        cursor = connection.cursor()
        sql_total = "SELECT SUM(subida_usu) AS subida, SUM(bajada_usu) AS bajada FROM cantidad_usuario_cantidadusuario"
        cursor.execute(sql_total,[])
        
        queryset = dictfetchall(cursor)
        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1
        data = json.dumps(response_data)
        return HttpResponse(data, content_type='application/json')
        
    
    # Proceso para mostrar la cantidad de totales wifi (Grafica)
    if accion == "mostrar":
    
        response_data = []
        cursor = connection.cursor()
        sql_sop = " SELECT hora, subida_usu, bajada_usu "
        sql_sop += " FROM cantidad_usuario_cantidadusuario WHERE date_create::date = '2015-10-02' ORDER BY id"
        cursor.execute(sql_sop,[])

        queryset = dictfetchall(cursor)
        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1
        
        data = json.dumps(response_data)
        
        return HttpResponse(data, content_type='application/json')
    
    # Proceso para mostrar la cantidad de totales wifi (Grafica)
    if accion == "graficaauto":

        response_data = []
        cursor = connection.cursor()
        sql_inc = " SELECT cantidad, hora "
        sql_inc += " FROM grafica_tabladinamica  ORDER BY id"
        cursor.execute(sql_inc,[])

        queryset = dictfetchall(cursor)

        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1

        data = json.dumps(response_data)
        
        return HttpResponse(data, content_type='application/json')
    
    if accion == "autoincrementado":
        
        # hora = time.strftime("%I:%M %p")
        hora = 'hola'
        # print hora
        aumento = random.randrange(10, 200, 5)
        # print "numero",aumento

        obj = TablaDinamica(
            cantidad = aumento,
            hora = hora,
        )
        obj.save()

    ctx = {}
    return render_to_response('reporte/reporte.html', ctx, context_instance=RequestContext(request))

def mostrar_dias(request):
    
    accion = request.POST.get('accion')
    
    # Proceso para mostrar la cantidad de totales wifi (Grafica)
    if accion == "mostrar_dias":
    
        response_data = []
        cursor = connection.cursor()
        sql_sop = " SELECT (CAST(date_create::date AS VARCHAR)) AS fecha, COUNT(*) AS total"
        sql_sop += " FROM cantidad_usuario_cantidadusuario GROUP BY date_create::date ORDER BY fecha ASC "
        cursor.execute(sql_sop,[])

        queryset = dictfetchall(cursor)
        print queryset
        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1
        
        data = json.dumps(response_data)
        print data
        
        return HttpResponse(data, content_type='application/json')
    ctx = {}
    return render_to_response('reporte/reporte_dia.html', ctx, context_instance=RequestContext(request))
    


def dictfetchall(cursor):
    """
    Metodo global para recorrer con el objeto dictfetchall (Clave Valor)
    """
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]