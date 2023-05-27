from django import forms
from terceraEntrega.models import Carrera, Alumno


class AlumnoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50
    )
    nombre.widget.attrs.update({
        'class':'form-control'
    })
    apellido = forms.CharField(
        label="Apellido",
        max_length=50
    )
    apellido.widget.attrs.update({
        'class':'form-control'
    })
    edad = forms.CharField(
        label="Edad",
        max_length=11
    )
    edad.widget.attrs.update({
        'class':'form-control'
    })
    email = forms.CharField(
        label="Email",
        max_length=50
    )
    email.widget.attrs.update({
        'class':'form-control'
    })

class RamoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50
    )
    nombre.widget.attrs.update({
        'class':'form-control'
    })
    carrera = forms.ModelChoiceField(queryset=Carrera.objects.all())
    carrera.widget.attrs.update({
        'class':'form-control'
    })

class CarreraForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50
    )
    nombre.widget.attrs.update({
        'class':'form-control'
    })

class BusquedaForm(forms.Form):
    search_text = forms.CharField(
        label="Buscar",
        max_length=50
    )
    search_text.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Alumno o carrera'
    })

class AsociarForm(forms.Form):
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.all())
    alumno.widget.attrs.update({
        'class':'form-control'
    })
    carrera = forms.ModelChoiceField(queryset=Carrera.objects.all())
    carrera.widget.attrs.update({
        'class':'form-control'
    })