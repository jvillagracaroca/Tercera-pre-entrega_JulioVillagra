from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('carreras', views.carreras, name="Carreras"),
    path('materias', views.materias, name="Materias"),
    path('asociar', views.asociar, name="Asociar"),
    path('tablaAlumnos', views.tablaAlumnos, name="TablaAlumnos"),
    path('tablaCarreras', views.tablaCarreras, name="TablaCarreras"),

]
