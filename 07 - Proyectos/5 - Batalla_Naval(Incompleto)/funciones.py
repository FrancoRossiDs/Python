from random import randint

#Tamaño del tablero
filas=5
columnas=5

#Inicializar tablero
tablero = [['O' for columnas in range(columnas)] for filas in range(filas)]


#Nombres inicializados
nombre_1 = ""
nombre_2 = ""

def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))



#Función para recibir nombres de los jugadores
def RecibirNombres():
    global nombre_1, nombre_2
    nombre_1 = input("Ingrese el nombre del primer jugador: ")
    nombre_2 = input("Ingrese el nombre del segundo jugador: ")
    return [nombre_1, nombre_2]

#Funciones para definir quien empieza a jugar
def EmpezarJuego():
    global nombre_1, nombre_2
    #Valores de los dados inicializados
    dado1 = 0
    dado2 = 0
    
    #Primer jugador tira su dado
    while True:
        dado_1r = input(f"{nombre_1}, ¿estás listo para tirar el dado? (Ingresa 'ya'): ").lower()
        if dado_1r == "ya":
            dado1 = Dado1()
            break
        else:
            print("Input incorrecto. Intenta de nuevo.")
    
    #Segundo jugador tira su dado
    while True:
        dado_2r = input(f"{nombre_2}, ¿estás listo para tirar el dado? (Ingresa 'ya'): ").lower()
        if dado_2r == "ya":
            dado2 = Dado2()
            break
        else:
            print("Input incorrecto. Intenta de nuevo.")
    
    #Se imprime el valor que se obtuvo de ambos dados con su jugador
    print(f"\n{nombre_1} ha obtenido {dado1} en el dado.")
    print(f"{nombre_2} ha obtenido {dado2} en el dado.")
    
    #se define quien empieza teniendo en cuenta el valor obtenido
    if dado1 > dado2:
        print(f"\n¡{nombre_1} va primero!")
    elif dado1 < dado2:
        print(f"\n¡{nombre_2} va primero!")
    else:
        print("\n¡Empate! Vuelvan a tirar los dados.")
        EmpezarJuego()

#Funciones para obtener el valor de lo dados
def Dado1():
    return randint(1, 6)
def Dado2():
    return randint(1, 6)


def colocar_barcos(nombres):
    global tablero, filas, columnas

    for jugador in range(2):
        nombre_jugador = nombres[jugador]

        print(f"\n{nombre_jugador}, es tu turno para colocar los barcos.")

        for barco in range(2):  # Colocar dos barcos por jugador
            while True:
                try:
                    print(f"\nTablero de {nombre_jugador}:")
                    mostrar_tablero(tablero)

                    print(f"\nColoca el {barco + 1}° barco.")

                    fila = int(input(f"Ingresa la fila inicial (0 a {filas - 1}): "))
                    columna = int(input(f"Ingresa la columna inicial (0 a {columnas - 3}): "))
                    orientacion = input("¿Quieres colocar el barco horizontalmente (h) o verticalmente (v)? ").lower()

                    if orientacion == 'h':
                        if 0 <= fila < filas and 0 <= columna < columnas - 2 and all(tablero[fila][col] == 'O' for col in range(columna, columna + 3)):
                            for col in range(columna, columna + 3):
                                tablero[fila][col] = f'B{jugador + 1}'  # Barco del jugador 1 se marca con 'B1', del jugador 2 con 'B2'
                            break
                        else:
                            print("Posición inválida. Elige una posición dentro del tablero y que no esté ocupada.")
                    elif orientacion == 'v':
                        if 0 <= fila < filas - 2 and 0 <= columna < columnas and all(tablero[row][columna] == 'O' for row in range(fila, fila + 3)):
                            for row in range(fila, fila + 3):
                                tablero[row][columna] = f'B{jugador + 1}'  # Barco del jugador 1 se marca con 'B1', del jugador 2 con 'B2'
                            break
                        else:
                            print("Posición inválida. Elige una posición dentro del tablero y que no esté ocupada.")
                    else:
                        print("Opción de orientación inválida. Ingresa 'h' para horizontal o 'v' para vertical.")
                except ValueError:
                    print("Ingresa números válidos.")

    # Mostrar el tablero después de que los jugadores hayan colocado sus barcos
    print("\nTablero después de que los jugadores colocaron sus barcos:")
    mostrar_tablero(tablero)



