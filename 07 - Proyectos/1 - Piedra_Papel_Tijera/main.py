from funciones import *

#Se pide nombre del usuario y la opcion que quiere ingresar (Piedra, Papel, Tijera)
print(" ")
global nombre
nombre = input("Ingrese su nombre\n")
RecibirNombre(nombre)
print(" ")
print(f"Bienvenido {nombre} al juego de Piedra Papel o Tijera!\n\nObtiene la victoria el primero en llegar a tres victorias")
print(" ")
""" respuesta=""
while respuesta!="no": """
#Bucle en donde la condicion es que haya un ganador
while True:
    if ComprobarVictoria(puntos_jugador,puntos_maquina):
        ResetVictoria()
        respuesta = input("¿Quiere jugar denuevo? si/no\n").lower()
        if respuesta=="no":
            break
    #Condición para que se ingrese un número del 1 al 3 
    try:
        elec = int(input("Ingrese su elección\n\n1: Piedra\n2: Papel\n3: Tijera\n\n"))
        if 1 <= elec <= 3:
            pass
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    #Se envia opción teniendo encuenta el índice
    if elec == 1:
        IgualdadOpciones(0)
    elif elec == 2:
        IgualdadOpciones(1)
    else:
        IgualdadOpciones(2)



