"""
Programa: eva02.py
Nombre completo (nombre primer_apellido segundo_apellido):
Matricula:
Fecha:
"""
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, genero, prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.prestado = prestado
        self.anio_publicacion = anio_publicacion
        self.genero = genero

    def prestar(self):
        self.prestado = True


    def devolver(self):
        self.delvover = False


    def mostrar_informacion(self):
        print(f"Título: {self.titulo}\n")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Prestado: {'Sí' if self.prestado else 'No'}")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción",True)
libro1.prestar()
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro1.devolver()
libro1.mostrar_informacion()
libro2.mostrar_informacion()
