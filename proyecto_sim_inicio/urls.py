from django.contrib import admin
from django.urls import path
from proyecto_sim_inicio import views

urlpatterns = [
    path ('', views.inicio),
    path ('mostrar_fecha/', views.mostrar_fecha),
    path ('saludo/<str:nombre>/<str:apellido>/', views.saludo),
    path ('mi_template/', views.mi_template),
    # path ('admin/', admin.site.urls)
]
