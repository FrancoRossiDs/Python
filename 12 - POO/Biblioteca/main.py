from libro import *
from biblioteca import *

from libro import Libro
from biblioteca import Biblioteca

import json
import os

def mostrar_menu():
    print("\nMenú:")
    print("1. Mostrar todos los libros disponibles.")
    print("2. Prestar un libro.")
    print("3. Recibir un libro.")
    print("4. Agregar un libro.")
    print("5. Quitar un libro.")
    print("6. Guardar datos de la biblioteca en un archivo JSON.")
    print("7. Cargar datos de la biblioteca desde un archivo JSON.")
    print("8. Salir.")

if __name__ == "__main__":
    biblioteca1 = Biblioteca()
    biblioteca2 = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            biblioteca1.mostrar_libros_disponibles()
        elif opcion == "2":
            titulo = input("Ingrese el título del libro que desea prestar: ")
            biblioteca1.prestar_libro(titulo)
        elif opcion == "3":
            titulo = input("Ingrese el título del libro que desea recibir: ")
            biblioteca1.recibir_libro(titulo)
        elif opcion == "4":
            titulo = input("Ingrese el título del nuevo libro: ")
            autor = input("Ingrese el autor del nuevo libro: ")
            año_publicacion = input("Ingrese el año de publicación del nuevo libro: ")
            unidades = input("Ingrese el número de unidades del nuevo libro: ")
            nuevo_libro = Libro(titulo, autor, año_publicacion, unidades)
            biblioteca1.agregar_libro(nuevo_libro)
        elif opcion == "5":
            titulo = input("Ingrese el título del libro que desea quitar: ")
            biblioteca1.quitar_libro(titulo)
        elif opcion == "6":
            nombre_archivo = input("Ingrese el nombre del archivo JSON para guardar los datos: ")
            biblioteca1.guardar_en_json(nombre_archivo)
        elif opcion == "7":
            nombre_archivo = input("Ingrese el nombre del archivo JSON para cargar los datos: ")
            biblioteca1.cargar_desde_json(nombre_archivo)
        elif opcion == "8":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.")

libro_1=Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 5)
