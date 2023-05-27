from django.shortcuts import redirect
from django.shortcuts import render
from terceraEntrega.forms import AlumnoForm, CarreraForm, RamoForm, BusquedaForm , AsociarForm
from terceraEntrega.models import Alumno, Carrera, Ramo, AlumnoCarrera
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


def home(request):        
    return render(request, "home.html")

def alumnos(request):
    alumnos = Alumno.objects.all()
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            alumno = Alumno(nombre = data["nombre"], apellido = data["apellido"], edad = data["edad"], email = data["email"])
            alumno.save()
            messages.success(request, 'El usuario se agregó correctamente.')
            form = AlumnoForm()    
            return redirect(request.path)
        
    else:
        form = AlumnoForm()     

    return render(request, "alumno.html", {"form":form, "alumnos":alumnos})

from terceraEntrega.models import Alumno, AlumnoCarrera

def tablaAlumnos(request):
    alumnos = Alumno.objects.all()
    paginator = Paginator(alumnos, 3)
    page = request.GET.get('page')
    try:
        alumnos_page = paginator.get_page(page)
    except PageNotAnInteger:
        alumnos_page = paginator.get_page(1)
    except EmptyPage:
        alumnos_page = paginator.get_page(paginator.num_pages)
    
    for alumno in alumnos_page:
        try:
            alumno_carreras = AlumnoCarrera.objects.filter(alumno=alumno)
            alumno.carreras_asociadas = [ac.carrera for ac in alumno_carreras]
        except AlumnoCarrera.DoesNotExist:
            alumno.carreras_asociadas = []

    return render(request, 'tablaAlumnos.html', {'alumnos_page': alumnos_page})


def carreras(request):
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            carrera = Carrera(nombre = data["nombre"])
            carrera.save()
            messages.success(request, 'La carrera se agregó correctamente.')
            form = CarreraForm()
            return redirect(request.path)
        
    else:
        form = CarreraForm()
    
    return render(request, "carrera.html", {"form":form, "carreras":carreras})
 
def tablaCarreras(request):
    carreras = Carrera.objects.all()
    paginator = Paginator(carreras, 6)  
    page = request.GET.get('page')
    try:
        carreras_page = paginator.get_page(page)
    except PageNotAnInteger:
        carreras_page = paginator.get_page(1)  
    except EmptyPage:
        carreras_page = paginator.get_page(paginator.num_pages)  
    return render(request, 'tablaCarreras.html', {'carreras_page': carreras_page})

def materias(request):
    materias = Ramo.objects.all()
    if request.method == 'POST':
        form = RamoForm(request.POST)
        if form.is_valid():  
            data = form.cleaned_data
            materia = Ramo(nombre=data["nombre"], carrera=data["carrera"])
            materia.save()
            messages.success(request, 'El ramo se agregó correctamente a la carrera.')
            form = RamoForm()
            return redirect(request.path)
    else:
        form = RamoForm()

    return render(request, "materia.html", {"form": form, "materias": materias})

def asociar(request):
    asociar = AlumnoCarrera.objects.all()
    if request.method == 'POST':
        form = AsociarForm(request.POST)
        if form.is_valid():  
            data = form.cleaned_data
            alumno = data["alumno"]
            carrera = data["carrera"]
            
            # Verificar si el registro ya existe en la base de datos
            if AlumnoCarrera.objects.filter(alumno=alumno, carrera=carrera).exists():
                messages.error(request, 'El registro ya existe en la base de datos.')
            else:
                asociar = AlumnoCarrera(alumno=alumno, carrera=carrera)
                asociar.save()
                messages.success(request, 'Se asoció correctamente el usuario a la carrera.')
                form = AsociarForm()
            
            return redirect(request.path)
    else:
        form = AsociarForm()

    return render(request, "alumnoCarrera.html", {"form": form, "asociar": asociar})
