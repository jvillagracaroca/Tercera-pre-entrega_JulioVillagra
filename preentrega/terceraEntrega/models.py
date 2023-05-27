from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.edad) + " " + self.email 



class Carrera(models.Model):
    nombre = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

class Ramo(models.Model):
    nombre = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.carrera.nombre

class AlumnoCarrera(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.alumno) + " - " + str(self.carrera)
