from django.contrib import admin
from django.urls import path, include
from proyecto_sim_inicio import views

app_name = 'entrega3'

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.inicio),
    path ('mostrar_fecha/', views.mostrar_fecha),
    path ('saludo/<str:nombre>/<str:apellido>/', views.saludo),
    path ('mi_template/', views.mi_template),
    path ('prueba_render/', views.prueba_render),    
]
