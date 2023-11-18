#lista de compras vacía
lista_compras={}

#factura vacía
factura={}

#lista de precios
precios={
    'Leche': 50,
    'Galletas': 35,
    'Gaseosa': 87,
    'Huevos': 66,
    'Aceite': 110,
    'Pan': 20
}

#lista de productos disponibles
productos_disp=["Leche", "Gaseosa", "Huevos", "Aceite", "Pan"]

#función para recibir nombre del usurario
def RecibirNombre():
    nombre_u=input()
    return nombre_u

#función para llenar la lista
def Llenarlistas(producto, cantidad):
    if producto in productos_disp:
        if producto not in lista_compras:
            lista_compras[producto] = cantidad
        else:
            lista_compras[producto] += cantidad
        print(f"{cantidad} unidades de {producto} agregadas a la lista\n")
    else:
        print(f"{producto} no es un producto válido.\n")

# función para corroborar elección y agregar a lista
def CorroborarLista():
    for item in productos_disp:
        respuesta = input(f"¿Quiere agregar {item} a su lista de compras? si/no\n").lower()
        if respuesta == "si":
            cantidad_valida = False
            while not cantidad_valida:
                cantidad_str = input("¿Cuántas unidades quiere agregar? ")
                if cantidad_str.isdigit():
                    cantidad = int(cantidad_str)
                    if cantidad > 0:
                        cantidad_valida = True
                    else:
                        print("Por favor, ingrese un número entero positivo.\n")
                else:
                    print("Por favor, ingrese un número entero válido.\n")
            Llenarlistas(item, cantidad)


#funcion para eliminar un producto seleccionado de la lista
def EliminarProducto():
    print("Lista actual:\n")
    for producto, cantidad in lista_compras.items():
        print(f"{producto}: {cantidad} unidades")

    producto_eliminar = input("\nIngrese el producto que desea eliminar o 'cancelar' para salir: \n").lower().capitalize()

    if producto_eliminar == 'Cancelar':
        print("Operación de eliminación cancelada.\n")
    elif producto_eliminar in lista_compras:
        del lista_compras[producto_eliminar]
        print(f"Producto {producto_eliminar} ha sido removido de la lista")
    else:
        print("Producto seleccionado no se encuentra en lista\n")


#función para mostrar la lista
def MostrarLista():
    print("\nLista de compras actual:\n")
    for producto, cantidad in lista_compras.items():
        print(f"{producto}: {cantidad} unidades")

#función para generar el precio total
def HacerCompra():
    print("Realizando Compra...\n")
    total=0
    for producto, cantidad in lista_compras.items():
        if producto in precios:
            total+=precios[producto]*cantidad
    return total

#función para generar factura
def GenerarFactura():
    print("Compra finalizada!\n")
    print("Su factura\n")
    suma = 0
    for producto, cantidad in lista_compras.items():
        subtotal = precios.get(producto, 0) * cantidad
        print(f"{producto}..........{cantidad} X {precios.get(producto, 0)} = {subtotal}")
        suma += subtotal
    print(f"Total a pagar..........{suma}\n")
