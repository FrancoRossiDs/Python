from random import randint
import sys
#Recibe nombre del jugador
def IngresarNombre():
    nombre = input("Ingrese su nombre\n")
    print(f"Bienvenido {nombre}\n")
    GenerarNumero()
#Genera numero aleatorio entre 1 y 100
def GenerarNumero():
    numero_m = randint(1, 100)
    Adivinar(numero_m)
#Genera numero del usuario
def GenerarNumeroUsuario():
    while True:
        numero = int(input("Ingrese en qué número estoy pensando: \n"))
        if 1 <= numero <= 100:
            return numero
        else:
            print("Ingrese un número válido. Estoy pensando en un número entre 1 y 100.\n")
#Funcion para comprobar si la elección del usuario es correcta
def Adivinar(numero_m):
    while True:
        vidas = 5

        while vidas != 0:
            #Si no adivina se actualiza elvalor de su elección
            numero_u = GenerarNumeroUsuario()

            if numero_u == numero_m:
                #En caso de ganar o perder se pregunta si quiere volver a empezar
                print(f"\n¡Felicitaciones! Adivinaste. Mi número era {numero_m}\n")
                respuesta = input("¿Desea volver a jugar? (si/no): ").lower()
                if respuesta == "no":
                    sys.exit()
                else:
                    GenerarNumero()
                    return
            #En caso de equivocarse devuelve si la elección era menor o mayor a la correcta
            elif numero_u < numero_m:
                print("El número es más grande!\n")
            else:
                print("El número es más pequeño\n")
            #Resta vidas 
            vidas -= 1
            print(f'Te quedan {vidas} vidas.\n')
        #Devolución en caso de perder. Tambien pregunta si quiere volver a empezar
        print(f"\nTe quedaste sin vidas. Mi número era {numero_m}. Mejor suerte para la próxima.\n")
        respuesta = input("¿Desea volver a jugar? (si/no): \n").lower()
        if respuesta == "no":
            sys.exit()
