#encoding:utf-8
import class_pdf
import sys
from django.db import connection, transaction
from django.conf import settings
from apps.script import delete_Files
import time


def reporte_expo(desde,hasta):

        reload(sys)
        sys.setdefaultencoding("utf-8")

        pdf = class_pdf.ReporteCandidato(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA
        year = time.strftime("%Y")
        pdf.set_author('Marcel Arcuri')
        pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
        pdf.add_page()  # ANADE UNA NUEVA PAGINACION
        pdf.set_margins(15,10,10)  # MARGENE DEL DOCUMENTO
        
        pdf.set_text_color(0,0,0)
        pdf.set_fill_color(255,255,255)
        pdf.set_y(7)
        pdf.set_x(85)
        pdf.write(30,"WIFI EXPO ARAGUA "+str(year).decode("UTF-8"))
        
        pdf.ln(30)
        pdf.set_text_color(0,0,0)
        pdf.set_fill_color(255, 255, 255)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(180,5,"Listado de usuarios conectados al wifi de la Expo Aragua Potencia "+str(year).decode("UTF-8"),'',1,'C',1)
        pdf.set_font('Arial', 'B', 10)
        pdf.ln(5)
        
        # Fila de la cabezara de la tabla
        # pdf.cell(10,5,"".decode("UTF-8"),'',0,'C',1)
        pdf.set_fill_color(0,0,0)
        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial','B',10)
        pdf.cell(20,5,"N°".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(25,5,"Usuarios".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(25,5,"Aumento".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(30,5,"Kb/s Bajada".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(30,5,"Kb/s Subida".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(55,5,"Hora".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.set_font('Arial','',10)

        cursor = connection.cursor()
        sql_det = "SELECT cantidad, subida_usu, bajada_usu, aumento, to_char(date_create, 'dd/mm/YYYY') as fecha_s, hora "
        sql_det += " FROM cantidad_usuario_cantidadusuario WHERE date_create  between %s and %s"
        sql_det += " ORDER BY id "
        # print sql_det
        cursor.execute(sql_det,[desde,hasta])
        row = dictfetchall(cursor)

        i = 1
        j = 0
        item = 0
        for t in row:
                # id_c = t['id_c']
                pdf.set_fill_color(255,255,255)
                if j == 33:
                        pdf.add_page()
                        pdf.set_text_color(0,0,0)
                        pdf.set_fill_color(255,255,255)
                        pdf.set_y(7)
                        pdf.set_x(85)
                        pdf.set_font('Arial', 'B', 16)
                        pdf.write(30,"WIFI EXPO ARAGUA 2015".decode("UTF-8"))
                        
                        pdf.ln(30)
                        pdf.set_text_color(0,0,0)
                        pdf.set_fill_color(255, 255, 255)
                        pdf.set_font('Arial', 'B', 12)
                        pdf.cell(180,5,"Listado de candidad de equipos conectados al wifi de la Expo Aragua Potencia 2015".decode("UTF-8"),'',1,'C',1)
                        pdf.set_font('Arial', 'B', 10)
                        pdf.ln(5)
                        
                        # Fila de la cabezara de la tabla
                        # pdf.cell(10,5,"".decode("UTF-8"),'',0,'C',1)
                        pdf.set_fill_color(0,0,0)
                        pdf.set_text_color(255,255,255)
                        pdf.set_font('Arial','B',10)
                        pdf.cell(20,5,"N°".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(25,5,"Usuarios".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(25,5,"Aumento".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(30,5,"Kb/s Bajada".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(30,5,"Kb/s Subida".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(55,5,"Hora".decode("UTF-8"),'LTBR',1,'C',1)
                        pdf.set_fill_color(255,255,255)
                        pdf.set_font('Arial','',10)
                        # Fin Cabezera
                        j=0
                item = int(item) + 1

                pdf.set_font('Arial','',8)
                pdf.set_fill_color(255,255,255)
                pdf.set_text_color(24,29,31)
                # pdf.cell(10,5,"".decode("UTF-8"),'',0,'C',1)
                pdf.cell(20,5,str(item).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(25,5,str(t['cantidad']).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(25,5,str(t['aumento']),'LTBR',0,'C',1)
                pdf.cell(30,5,str(t['subida_usu'])+' Kb/s','LTBR',0,'C',1)
                pdf.cell(30,5,str(t['bajada_usu'])+' Kb/s'.decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(55,5,str(t['fecha_s'])+' '+str(t['hora']),'LTBR',1,'C',1)
                j = j + 1
                
        
        cursor = connection.cursor()
        sql_tot = "SELECT SUM(aumento) AS aumento_t, SUM(subida_usu) AS subida_t, SUM(bajada_usu) AS bajada_t  "
        sql_tot += " FROM cantidad_usuario_cantidadusuario WHERE date_create  between %s and %s"
        cursor.execute(sql_tot,[desde,hasta])
        row = dictfetchall(cursor)
        
        aumento_t = row[0]['aumento_t']
        subida_t = row[0]['subida_t']
        bajada_t = row[0]['bajada_t']
        
        # pdf.set_text_color(24,29,31)
        # pdf.set_font('Arial','B',9)
        # pdf.set_fill_color(191,191,191)
        # pdf.cell(20,5,"TOTALES".decode("UTF-8"),'LTBR',0,'C',1)
        # pdf.cell(25,5,str(aumento_t),'LTBR',0,'C',1)
        # pdf.cell(25,5,str(subida_t)+"KB/s DE SUBIDA",'LTBR',0,'C',1)
        # pdf.cell(30,5,str(bajada_t)+' KB/s DE BAJADA'.decode("UTF-8"),'LTBR',1,'C',1)
        
        pdf.ln(10)
        pdf.set_text_color(24,29,31)
        pdf.set_font('Arial','B',9)
        pdf.set_fill_color(0,0,0)
        pdf.set_text_color(255,255,255)
        pdf.cell(185,5,"TOTALES GENERALES".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_text_color(24,29,31)
        pdf.set_fill_color(191,191,191)
        pdf.cell(31,5,"USUARIOS".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.cell(30,5,str(aumento_t),'LTBR',0,'C',1)
        pdf.set_fill_color(191,191,191)
        pdf.cell(32,5,"KB/s DE BAJADA".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.cell(30,5,str(subida_t)+' Kb/s','LTBR',0,'C',1)
        pdf.set_fill_color(191,191,191)
        pdf.cell(32,5,"KB/s DE SUBIDA".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.cell(30,5,str(bajada_t)+' Kb/s'.decode("UTF-8"),'LTBR',1,'C',1)

        cursor = connection.cursor()
        sql_sop = " SELECT (CAST(date_create::date AS VARCHAR)) AS fecha, COUNT(*) AS total"
        # sql_sop += " SUM(subida_usu) AS sub, SUM(bajada_usu) AS baj, "
        sql_sop += " FROM cantidad_usuario_cantidadusuario GROUP BY date_create::date ORDER BY fecha ASC "
        cursor.execute(sql_sop)
        row2 = dictfetchall(cursor)
        
        pdf.ln(5)
        
        pdf.set_font('Arial','B',9)
        pdf.set_fill_color(0,0,0)
        pdf.set_text_color(255,255,255)
        pdf.cell(40,5,"TOTALES DIARIOS".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(191,191,191)
        pdf.set_text_color(24,29,31)
        pdf.cell(20,5,"DÍA".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"USUARIOS".decode("UTF-8"),'LTBR',1,'C',1)
        
        for m in row2:
                dias = m['fecha']
                dia = dias.split('-')
                pdf.set_fill_color(191,191,191)
                pdf.cell(20,5,str(dia[2])+' Octubre','LTBR',0,'C',1)
                pdf.set_fill_color(255,255,255)
                pdf.cell(20,5,str(m['total']).decode("UTF-8"),'LTBR',1,'C',1)
        
        
        ruta_reporte = settings.MEDIA_PDF
        nombre = ' Detallado.pdf'
        pdf.output(ruta_reporte+'/'+nombre, 'F')
        archivo = open(ruta_reporte+'/'+nombre, "r")

        ruta = ruta_reporte+'/'
        delete_Files(ruta)
        
        return nombre, archivo


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
