from funciones import *

# Se le pide nombre al usuario
print("\nBienvenido, ingrese su nombre\n")
nombre = RecibirNombre()

while True:
    print("¿Qué desea hacer?\n")
    seleccion = input("1. Crear/Modificar Lista\n2. Eliminar producto de lista\n3. Ver lista de compras\n4. Finalizar compra\n5. Salir\n")

    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= 5:
            if seleccion == 1:
                CorroborarLista()
                print(f"\nLista de compras finalizada\n")
                print(lista_compras)
                modificar = input(f"{nombre}, ¿Desea modificar la lista? si/no\n").lower()
                if modificar == "si":
                    CorroborarLista()
                    print(f"\nLista de compras actualizada:\n")
                    print(lista_compras)
            elif seleccion == 2:
                EliminarProducto()
            elif seleccion == 3:
                MostrarLista()
            elif seleccion == 4:
                GenerarFactura()
            else:
                break
        else:
            print("Ingrese un número entre 1 y 5\n")
    else:
        print("Por favor, ingrese un número entero válido.\n")

# Fuera del bucle, después de salir
print(f"Gracias {nombre} por usar nuestro servicio de carrito de compras!\n")


