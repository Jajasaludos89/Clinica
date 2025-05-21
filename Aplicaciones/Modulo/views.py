from django.shortcuts import render, redirect
from .models import Empleado, AveDePresa, SesionFisioterapia
from django.contrib import messages


#Empleado

def inicioEmpleados(request):
    empleados = Empleado.objects.all()
    return render(request, "inicioEmpleados.html", {'empleados': empleados})

def nuevoEmpleado(request):
    return render(request, "nuevoEmpleado.html")

def guardarEmpleado(request):
    identificacion = request.POST["identificacion"]
    nombre = request.POST["nombre"]
    edad = request.POST["edad"]
    titulo = request.POST["titulo"]
    especialidad = request.POST["especialidad"]

    Empleado.objects.create(
        identificacion=identificacion,
        nombre=nombre,
        edad=edad,
        titulo=titulo,
        especialidad=especialidad
    )

    messages.success(request, "Empleado GUARDADO exitosamente")
    return redirect('/empleados')

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    messages.success(request, "Empleado ELIMINADO exitosamente")
    return redirect('/empleados')

def editarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request, "editarEmpleado.html", {'empleado': empleado})

def procesarEdicionEmpleado(request):
    id = request.POST["id"]
    empleado = Empleado.objects.get(id=id)
    empleado.identificacion = request.POST["identificacion"]
    empleado.nombre = request.POST["nombre"]
    empleado.edad = request.POST["edad"]
    empleado.titulo = request.POST["titulo"]
    empleado.especialidad = request.POST["especialidad"]
    empleado.save()
    messages.success(request, "Empleado ACTUALIZADO exitosamente")
    return redirect('/empleados')
