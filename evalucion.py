"""
Programa: eva01.py
Alumno:leydi
Matricula:8932
Fecha:12-24-32
"""

class Profesores():
    id = None
    nombre = ""
    materias = []


    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        print("Constructor objeto" , "Profesor")


    def califica(self):
        print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre,self.materias[0]))


    def pasaAsistencia(self):
        print(f"El profesor {self.nombre} pasa asistencia")




profesor1 = Profesores("111","Profesor 1")
profesor1.materias.append("Materia 1")
profesor1.materias.append("Materia 2")#llama al metodo califica
profesor1.califica()#llama al metodo que califica

profesor1.pasaAsistencia()#llama al metodo pasaasistencia
