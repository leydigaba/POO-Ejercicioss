"""
   Nombre: Leydi Jaret Gallegos Badillo
   Fecha: 18/01/2024
   Descripcion: Programa que define un objeto con el metodo init
"""

class A: # Define una clase de nombre
    matricula = None # Declara la varible de la matricula
    nombre = None # Declara la variable del nombre
    def __init__(self,matricula,nombre): # Define el constructo y asigna los valores de la matricula y el nombre
        print("contructor de la clase A") #Imprime el mensaje
        self.matricula=matricula #Asigna a la variable la matricula
        self.nombre=nombre #asigna a la variable el valordel nombre
objetoA=A(1111,"Dejah") #Genera un objeto de la clase A con los valores de la matricula y el nombre
print(objetoA.nombre) #Imprime la variable del nombre del objeto
