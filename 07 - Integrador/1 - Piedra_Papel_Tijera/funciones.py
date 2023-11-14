from random import randint

opciones = ["Piedra", "Papel", "Tijera"]
puntos_jugador = 0
puntos_maquina = 0
c = 0
victoria=False
def RecibirNombre(nombre):
    global name
    name=nombre

def IgualdadOpciones(indice):
    global c, puntos_jugador, puntos_maquina
    indice_r = OpcionRobot()
    if opciones[indice] == opciones[indice_r]:
        print(" ")
        print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nEmpate, nadie se lleva punto\n")
    else:
        c += 1
        Comparacion(indice, indice_r)
        if c>=3:
            ComprobarVictoria(puntos_jugador,puntos_maquina)

def OpcionRobot():
    return randint(0, 2)

def ComprobarVictoria(puntos_jugador, puntos_maquina):
    global victoria
    if puntos_jugador == 3 or puntos_maquina == 3:
        if puntos_jugador == 3:
            print(f"{name} ganó. ¡Felicidades!")
            print(" ")
            victoria=True
        else:
            print("CPU ganó, mejor suerte la próxima!")
            print(" ")
            victoria=True
    return victoria

def Comparacion(indice, indice_r):
    global puntos_jugador, puntos_maquina
    if abs(indice - indice_r) == 1:
        if indice > indice_r:
            print(" ")
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para {name}")
            print(" ")
            puntos_jugador += 1
        else:
            print(" ")
            puntos_maquina += 1
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para CPU")
            print(" ")
    if abs(indice - indice_r) == 2:
        if indice > indice_r:
            print(" ")
            puntos_maquina += 1
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para CPU")
            print(" ")
        else:
            print(" ")
            puntos_jugador += 1
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para {name}")
            print(" ")