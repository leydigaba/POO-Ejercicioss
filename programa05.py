"""
   Nombre: Leydi Jaret Gallegos Badillo
   Fecha: 18/01/2024
   Descripcion: Programa que define a un objeto "Alumnos" 
"""


class Alumno: #Define la clase del alumno
    
    nombre = None #Define la variable del nombre
    matricula = None #Define la variable de la matricula 

    def __init__(self,nombre,matricula): #Define la funcion de la clase
        self.matricula = matricula #Define la variable del matricula
        self.nombre = nombre #Define la variable del nombre
        print("objeto Alumno") #crea un objeto Alumno

    def estudiar(self): #Define la funcion de la clase
        print(f"{self.nombre} estudia") #Imprime el nombre del alumno y la funcion de estudia
    def sumar (self,numero1,numero2): #Define la funcion de la clase
        suma = numero1 + numero2 #Define la variable de la suma de los dos numeros
        print(f"¨{numero1}+{numero2}={suma}") #Crea la suma de los dos numeros

dejah=Alumno(1723110576,"Dejah") #Imprime el nombre de la matricula y el nombre del alumno
dejah.estudiar () # Imprime la funcion de estudiar
dejah.sumar(10,5) #imprime la suma de los dos numeros
print(f"La matricula del alumno es{dejah.matricula}") #Imprime la matricula del alumno
