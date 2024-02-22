"""
   Nombre: Leydi Jaret Gallegos Badillo
   Fecha: 18/01/2024
   Descripcion: Programa que define un objeto pero no lo llama, ya que no se esta asignadas las variables
"""

class Alumnos: #Define la clase de los alumnos
    matricula = None #Define la varible de matricula
    nombre = None #Define la variable del nombre
    def __init__(self, matricula, nombre): #Define el constructor y asigna los valores de la matricula y el nombre
      self.matricula = matricula # Asigna a la variable el valor de matricula
      self.nombre = nombre #Asigna a la variable el valor del nombre
      print("objeto Alumnos") #Imprime el objeto alumno
objetoAlumnos = Alumnos()#Genera un objeto de la clase Alumnos
