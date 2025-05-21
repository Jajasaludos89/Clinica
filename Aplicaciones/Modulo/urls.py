from django.urls import path
from . import views

urlpatterns = [
    path('empleados', views.inicioEmpleados),
    path('nuevoEmpleado', views.nuevoEmpleado),
    path('guardarEmpleado', views.guardarEmpleado),
    path('eliminarEmpleado/<id>', views.eliminarEmpleado),
    path('editarEmpleado/<id>', views.editarEmpleado),
    path('procesarEdicionEmpleado', views.procesarEdicionEmpleado),

]
