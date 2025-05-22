from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicioEmpleados),

    path('empleados', views.inicioEmpleados),
    path('nuevoEmpleado', views.nuevoEmpleado),
    path('guardarEmpleado', views.guardarEmpleado),
    path('eliminarEmpleado/<id>', views.eliminarEmpleado),
    path('editarEmpleado/<id>', views.editarEmpleado),
    path('procesarEdicionEmpleado', views.procesarEdicionEmpleado),

    path('aves', views.inicioAves),
    path('nuevaAve', views.nuevaAve),
    path('guardarAve', views.guardarAve),
    path('eliminarAve/<id>', views.eliminarAve),
    path('editarAve/<id>', views.editarAve),
    path('procesarEdicionAve', views.procesarEdicionAve),

    path('sesiones', views.inicioSesiones),
    path('nuevaSesion', views.nuevaSesion),
    path('guardarSesion', views.guardarSesion),
    path('eliminarSesion/<id>', views.eliminarSesion),
    path('editarSesion/<id>', views.editarSesion),
    path('procesarEdicionSesion', views.procesarEdicionSesion),

]
