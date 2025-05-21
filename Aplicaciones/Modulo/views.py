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

#ave

def inicioAves(request):
    aves = AveDePresa.objects.all()
    return render(request, "inicioAves.html", {'aves': aves})

def nuevaAve(request):
    return render(request, "nuevaAve.html")

def guardarAve(request):
    nombre = request.POST["nombre"]
    especie = request.POST["especie"]
    fecha_ingreso = request.POST["fecha_ingreso"]
    observaciones = request.POST["observaciones"]

    AveDePresa.objects.create(
        nombre=nombre,
        especie=especie,
        fecha_ingreso=fecha_ingreso,
        observaciones=observaciones
    )

    messages.success(request, "Ave GUARDADA exitosamente")
    return redirect('/aves')

def eliminarAve(request, id):
    ave = AveDePresa.objects.get(id=id)
    ave.delete()
    messages.success(request, "Ave ELIMINADA exitosamente")
    return redirect('/aves')

def editarAve(request, id):
    ave = AveDePresa.objects.get(id=id)
    return render(request, "editarAve.html", {'ave': ave})

def procesarEdicionAve(request):
    id = request.POST["id"]
    ave = AveDePresa.objects.get(id=id)
    ave.nombre = request.POST["nombre"]
    ave.especie = request.POST["especie"]
    ave.fecha_ingreso = request.POST["fecha_ingreso"]
    ave.observaciones = request.POST["observaciones"]
    ave.save()
    messages.success(request, "Ave ACTUALIZADA exitosamente")
    return redirect('/aves')

