from random import randint
import sys

def IngresarNombre():
    nombre = input("Ingrese su nombre\n")
    print(f"Bienvenido {nombre}\n")
    GenerarNumero()

def GenerarNumero():
    numero_m = randint(1, 100)
    Adivinar(numero_m)

def GenerarNumeroUsuario():
    while True:
        numero = int(input("Ingrese en qué número estoy pensando: \n"))
        if 1 <= numero <= 100:
            return numero
        else:
            print("Ingrese un número válido. Estoy pensando en un número entre 1 y 100.\n")

def Adivinar(numero_m):
    while True:
        vidas = 5

        while vidas != 0:
            numero_u = GenerarNumeroUsuario()

            if numero_u == numero_m:
                print(f"\n¡Felicitaciones! Adivinaste. Mi número era {numero_m}\n")
                respuesta = input("¿Desea volver a jugar? (si/no): ").lower()
                if respuesta == "no":
                    sys.exit()
                else:
                    GenerarNumero()
                    return
            elif numero_u < numero_m:
                print("El número es más grande!\n")
            else:
                print("El número es más pequeño\n")
            
            vidas -= 1
            print(f'Te quedan {vidas} vidas.\n')

        print(f"\nTe quedaste sin vidas. Mi número era {numero_m}. Mejor suerte para la próxima.\n")
        respuesta = input("¿Desea volver a jugar? (si/no): \n").lower()
        if respuesta == "no":
            sys.exit()
