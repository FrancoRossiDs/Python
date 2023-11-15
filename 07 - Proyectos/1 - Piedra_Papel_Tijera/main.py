from funciones import *


print(" ")
global nombre
nombre = input("Ingrese su nombre\n")
RecibirNombre(nombre)
print(" ")
print(f"Bienvenido {nombre} al juego de Piedra Papel o Tijera!\n\nObtiene la victoria el primero en llegar a tres victorias")
print(" ")
""" respuesta=""
while respuesta!="no": """
while not ComprobarVictoria(puntos_jugador,puntos_maquina):
    while True:
        try:
            elec = int(input("Ingrese su elección\n\n1: Piedra\n2: Papel\n3: Tijera\n\n"))
            if 1 <= elec <= 3:
                break
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    if elec == 1:
        IgualdadOpciones(0)
    elif elec == 2:
        IgualdadOpciones(1)
    else:
        IgualdadOpciones(2)

    """ respuesta = input("¿Quiere jugar denuevo? si/no\n").lower()
    if respuesta=="si":
        victoria=False """


