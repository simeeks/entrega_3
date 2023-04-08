from django.shortcuts import render

def inicio(request):
    return render(request, 'proyecto_sim_inicio/inicio.html')
