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

#secion

def inicioSesiones(request):
    sesiones = SesionFisioterapia.objects.all()
    return render(request, "inicioSesiones.html", {'sesiones': sesiones})

def nuevaSesion(request):
    empleados = Empleado.objects.all()
    aves = AveDePresa.objects.all()
    return render(request, "nuevaSesion.html", {'empleados': empleados, 'aves': aves})

def guardarSesion(request):
    fisioterapeuta_id = request.POST["fisioterapeuta"]
    ave_id = request.POST["ave"]
    fecha_sesion = request.POST["fecha_sesion"]
    descripcion = request.POST["descripcion"]

    SesionFisioterapia.objects.create(
        fisioterapeuta_id=fisioterapeuta_id,
        ave_id=ave_id,
        fecha_sesion=fecha_sesion,
        descripcion=descripcion
    )

    messages.success(request, "Sesión GUARDADA exitosamente")
    return redirect('/sesiones')

def eliminarSesion(request, id):
    sesion = SesionFisioterapia.objects.get(id=id)
    sesion.delete()
    messages.success(request, "Sesión ELIMINADA exitosamente")
    return redirect('/sesiones')

def editarSesion(request, id):
    sesion = SesionFisioterapia.objects.get(id=id)
    empleados = Empleado.objects.all()
    aves = AveDePresa.objects.all()
    return render(request, "editarSesion.html", {'sesion': sesion, 'empleados': empleados, 'aves': aves})

def procesarEdicionSesion(request):
    id = request.POST["id"]
    sesion = SesionFisioterapia.objects.get(id=id)
    sesion.fisioterapeuta_id = request.POST["fisioterapeuta"]
    sesion.ave_id = request.POST["ave"]
    sesion.fecha_sesion = request.POST["fecha_sesion"]
    sesion.descripcion = request.POST["descripcion"]
    sesion.save()
    messages.success(request, "Sesión ACTUALIZADA exitosamente")
    return redirect('/sesiones')