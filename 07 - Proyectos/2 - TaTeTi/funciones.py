from random import randint

tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def ResetearTablero():
    for n in range(len(tablero)):
        for i in range(len(tablero[0])):
            tablero[i][n]= " "

lista_lugares = [str(i + 1) for i in range(9)]

nombre_1 = ""
nombre_2 = ""
c=0

def MostrarTableroConNumeros():
    # Diccionario para mapear las posiciones a sus valores
    mapping = {1: [0, 0], 2: [0, 1], 3: [0, 2],
               4: [1, 0], 5: [1, 1], 6: [1, 2],
               7: [2, 0], 8: [2, 1], 9: [2, 2]}

    # Tablero con números y X/O
    print("\nTablero con números:\n")
    for i in range(1, 10, 3):
        row = [tablero[mapping[num][0]][mapping[num][1]] for num in range(i, i + 3)]
        print(" | ".join(str(cell) if cell != " " else str(num) for num, cell in zip(range(i, i + 3), row)))
        if i < 7:
            print("-" * 10)


def ActualizarLista():
    global lista_lugares
    lista_lugares = [str(i + 1) for i in range(9) if tablero[i // 3][i % 3] == " "]

# En funciones.py

def RecibirNombres():
    global nombre_1, nombre_2
    print(" ")
    nombre_1=input("Ingrese el nombre del primer jugador\n")
    nombre_2=input("Ingrese el nombre del segundo jugador\n")


def MostrarTablero():
    for i in range(len(tablero)):
        print(tablero[i])
    return ''


def QuienEmpieza():
    dado_r = ""
    dado_r2 = ""

    while dado_r.lower() != "ya":
        dado_r = input(f"\n{nombre_1} arroje su dado cuando esté listo (Ya para arrojar)\n").lower()
    
    dado1 = ArrojarDado1()
    print(f"Resultado {dado1}\n")
    
    while dado_r2.lower() != "ya":
        dado_r2 = input(f"\n{nombre_2} arroje su dado cuando esté listo (Ya para arrojar)\n").lower()

    dado2 = ArrojarDado2()
    print(f"Resultado {dado2}\n")
    
    if dado1 > dado2:
        EmpiezaUno()
    elif dado2>dado1:
        EmpiezaDos()
    else:
        print("Empate\n")
        QuienEmpieza()


def ArrojarDado1():
    return randint(1, 6)

def ArrojarDado2():
    return randint(1, 6)

def EmpiezaUno():
    global c
    c += 1
    eleccion1 = ""
    while eleccion1 != "3":
        eleccion1 = input(f"\n{nombre_1} haga su movimiento\n1: Ver estado del tablero\n2: Ver lista de opciones\n3: Hacer movimientos\n")
        if eleccion1 == "1":
            MostrarTablero()
        elif eleccion1 == "2":
            # actualiza los lugares y elimina los que esten ocupados de las opciones
            ActualizarLista()
            MostrarTableroConNumeros()
            print(f"\nElecciones disponibles para {nombre_1}: {', '.join(lista_lugares)}\n")
        elif eleccion1 == "3":
            while True:
                try:
                    eleccion_lugar = int(input(f"Elija una opción: \n"))
                    if eleccion_lugar < 1 or eleccion_lugar > 9:
                        raise ValueError("No existe opción. Intente de nuevo.\n")

                    fila, columna = divmod(eleccion_lugar - 1, 3)
                    # Verifica si la casilla está vacía
                    if tablero[fila][columna] == ' ':
                        # Completa la casilla con la ficha correspondiente
                        tablero[fila][columna] = 'X'
                        if c >= 3:
                            resultado = ComprobarGanador()
                            if resultado:
                                print(resultado)
                                respuesta=input("¿Quieren volver a jugar?")
                                if respuesta!="no":
                                    ResetearTablero()
                                    QuienEmpieza()
                        break
                    else:
                        print("Casilla ocupada. Intente de nuevo.\n")
                except ValueError as e:
                    print(f"Error: {e}")
        else:
            print("¡Opción inválida! Por favor, elija 1, 2 o 3.\n")

    EmpiezaDos()

def EmpiezaDos():
    global c
    c += 1
    eleccion2 = ""
    while eleccion2 != "3":
        eleccion2 = input(f"\n{nombre_2} haga su movimiento\n1: Ver estado del tablero\n2: Ver lista de opciones\n3: Hacer movimientos\n")
        if eleccion2 == "1":
            MostrarTablero()
        elif eleccion2 == "2":
            # actualiza los lugares y elimina los que esten ocupados de las opciones
            ActualizarLista()
            MostrarTableroConNumeros()
            print(f"\nElecciones disponibles para {nombre_2}: {', '.join(lista_lugares)}\n")
        elif eleccion2 == "3":
            while True:
                try:
                    # Pide al jugador que elija una opción
                    eleccion_lugar = int(input(f"Elija una opción: \n"))
                    if eleccion_lugar < 1 or eleccion_lugar > 9:
                        raise ValueError("No existe opción. Intente de nuevo.\n")

                    fila, columna = divmod(eleccion_lugar - 1, 3)
                    # Verifica si la casilla está vacía
                    if tablero[fila][columna] == ' ':
                        # Completa la casilla con la ficha correspondiente
                        tablero[fila][columna] = 'O'
                        if c >= 3:
                            resultado = ComprobarGanador()
                            if resultado:
                                print(resultado)
                                respuesta=input("¿Quieren volver a jugar?")
                                if respuesta!="no":
                                    ResetearTablero()
                                    QuienEmpieza()
                        break
                    else:
                        print("Casilla ocupada. Intente de nuevo.\n")
                except ValueError as e:
                    print(f"Error: {e}")
        else:
            print("¡Opción inválida! Por favor, elija 1, 2 o 3.\n")

    EmpiezaUno()





def ComprobarGanador():
    for fila in tablero:
        if fila.count('X') == 3:
            MostrarTablero()
            return f'\nGanador: {nombre_1}!\n'
        elif fila.count('O') == 3:
            MostrarTablero()
            return f'\nGanador: {nombre_2}!\n'

    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] == 'X':
            MostrarTablero()
            return f'\nGanador: {nombre_1}!\n'
        elif tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] == 'O':
            MostrarTablero()
            return f'\nGanador: {nombre_2}!\n'

    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] == 'X':
        MostrarTablero()
        return f'\nGanador: {nombre_1}!\n'
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] == 'X':
        MostrarTablero()
        return f'\nGanador: {nombre_1}!\n'
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] == 'O':
        MostrarTablero()
        return f'\nGanador: {nombre_2}!\n'
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] == 'O':
        MostrarTablero()
        return f'\nGanador: {nombre_2}!\n'

    if all(all(casilla != ' ' for casilla in fila) for fila in tablero):
        MostrarTablero
        return '\nEmpate!\n'
    
    return None


