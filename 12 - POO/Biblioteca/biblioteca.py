from libro import *
import json

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []
    
    def mostrar_libros_disponibles(self):
        print("Libros disponibles:")
        for libro in self.libros_disponibles:
            print(f"{libro.titulo} - {libro.autor} - Disponible: {libro.disponible}")
    
    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f"Libro '{titulo}' prestado con éxito.")
                return
        print(f"El libro '{titulo}' no está disponible para préstamo.")
    
    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f"Libro '{titulo}' devuelto con éxito.")
                return
        print(f"No se puede recibir el libro '{titulo}'.")
    
    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
    
    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                print(f"Libro '{titulo}' eliminado de la biblioteca.")
                return
        print(f"No se puede encontrar el libro '{titulo}' en la biblioteca.")

    def guardar_en_json(self, nombre_archivo):
        libros_data = []
        for libro in self.libros_disponibles:
            libro_data = {
                "titulo": libro.titulo,
                "autor": libro.autor,
                "año_publicacion": libro.año_publicacion,
                "unidades": libro.unidades,
                "disponible": libro.disponible
            }
            libros_data.append(libro_data)

        with open(nombre_archivo, 'w') as json_file:
            json.dump(libros_data, json_file)
        print(f"Datos de la biblioteca guardados en {nombre_archivo}.")

    def cargar_desde_json(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as json_file:
                libros_data = json.load(json_file)
                for libro_data in libros_data:
                    libro = libro(
                        titulo=libro_data["titulo"],
                        autor=libro_data["autor"],
                        año_publicacion=libro_data["año_publicacion"],
                        unidades=libro_data["unidades"]
                    )
                    libro.disponible = libro_data["disponible"]
                    self.libros_disponibles.append(libro)
            print(f"Datos de la biblioteca cargados desde {nombre_archivo}.")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")



