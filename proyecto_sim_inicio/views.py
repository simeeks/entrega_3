from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    return render(request, 'proyecto_sim_inicio/index.html')

def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    return HttpResponse(f' <p>{dt_formateado} </p>')

def saludo(request, nombre, apellido):
    return HttpResponse(f'<h1>Hola {nombre} {apellido}</h1>')

def mi_template(request):
    
    archivo = open(r'C:\Datos\CODERHOUSE\entrega_3\templates\mi_template.html')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def prueba_render(request):
    return render(request, r'C:\Datos\CODERHOUSE\entrega_3\templates\prueba_render.html')

def index(request):
    return render(request, r'C:\Datos\CODERHOUSE\entrega_3\proyecto_sim_inicio\templates\proyecto_sim_inicio\index.html')