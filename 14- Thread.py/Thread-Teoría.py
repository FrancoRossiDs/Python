"""Paso 1. Pip install auto-py-to-exe """
"""Paso 2. auto-py-to-exe """
"""Paso 3.  threading"""
"""Paso 4. import time """
import threading
import time

def hola(bandera):
    while not bandera.is_set():
        print("\nEjecución en segundo plano...", end="\r")
        time.sleep(3)


bandera=threading.Event()
hilo=threading.Thread(target=hola, args=(bandera,))
hilo.start()

while True:
    entrada=input("\nPresione una tecla para detener la ejecución\n1)Comer\n2)Jugar\n3)Salir")
    
    if entrada:
        bandera.set()
        hilo.join()
        break