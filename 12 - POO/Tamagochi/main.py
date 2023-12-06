from clases import *
#Se ingrese el nombre de la mascota
nombre=input("Ingrese el nombre de su mascota virtual \n")

#Se inicia la clase con su nombre
mascota = Tamagochi(nombre)
hilo=mascota.iniciarTamagotchi()
bandera=threading.Event()


#Bucle while que se repetirá mientras la mascota esté viva(esta_vivo = True) o se eliga la opción de salir (5)
while mascota.esta_vivo:
    #Opciones para interactuar con la Mascota
    print("\n¿Qué quieres hacer?")
    print("1. Ver estado")
    print("2. Alimentar")
    print("3. Jugar")
    print("4. Dormir")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): \n")
    #If con las opciones
    if opcion == "1":
        mascota.mostrar_estado()
    elif opcion == "2":
        mascota.alimentar()
    elif opcion == "3":
        mascota.jugar()
    elif opcion == "4":
        mascota.dormir()
    elif opcion == "5":
        bandera.set()
        hilo.join()
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")