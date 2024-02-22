"""
   Nombre: Leydi Jaret Gallegos Badillo
   Fecha: 18/01/2024
   Descripcion: Programa que define a un objeto "Alumnos" 
"""


class Alumnos: #Define la case de los alumnos
    matricula = None #Define la variable de matricula
    nombre = None #Define la variable del nombre 
    def __init__(self, matricula, nombre): #Define el constructor y asigna los valores de la matricula y el nombre
        self.matricula = matricula #Asigna el valor de la matricula
        self.nombre = nombre #Asigna el valor del nombre
        print("objeto Alumnos") #Imprime el objeto alumno
objetoAlumnos = Alumnos (111,"Dejah") #Genera un objeto de la clase Alumnos con los valores de la matricula y el nombre 
objetoAlumnos = Alumnos (nombre = "Jhon",matricula = 222) #Genera un objeto de la clase Alumnos donde se les asigna los valores de la matricula y el nombre
