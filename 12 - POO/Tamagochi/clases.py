import threading
import time
from clases import *

class Tamagochi:
    #Valores iniciales de la mascota
    def __init__(self, nombre, tiempo_de_espera=3):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True
        self.tiempo_de_espera = tiempo_de_espera

    #Función para mostrar el estado actual de la mascota
    def mostrar_estado(self):
        print(f"{self.nombre}:")
        print(f"Nivel de Energía: {self.nivel_energia}")
        print(f"Nivel de Hambre: {self.nivel_hambre}")
        print(f"Estado de Humor: {self.humor}")
        print()

    #Función para alimentar mascota(Resta hambre y energía)
    def alimentar(self):
        if self.esta_vivo:
            self.nivel_hambre -= 10
            self.nivel_energia -= 15
            self.actualizar_valores()
            self.actualizar_humor()
            self.verificar_estado()

    #Función para jugar con mascota(Suma felicidad, Resta energía, Suma hambre)
    def jugar(self):
        if self.esta_vivo:
            self.nivel_felicidad += 20
            self.nivel_energia -= 18
            self.nivel_hambre += 10
            self.actualizar_valores()
            self.actualizar_humor()
            self.verificar_estado()

    #Función para hacer dormir a la  mascota(Suma energía, Suma hambre)
    def dormir(self):
        if self.esta_vivo:
            self.nivel_energia += 40
            self.nivel_hambre += 5
            self.actualizar_valores()
            self.actualizar_humor()
            self.verificar_estado()

    #Función que verifica el estado de la mascota, en caso de que tenga mas de 50 de hambre como "castigo" resta automanticamente felicidad y energía
    def verificar_estado(self):
        if self.nivel_hambre >= 50:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
            self.actualizar_valores()
            self.actualizar_humor()
        #En caso de que la energía llegue a 0 la mascota muere
        if self.nivel_energia == 0:
            self.esta_vivo = False
            print(f"{self.nombre} ha muerto. ¡Descansa en paz!")

    #Funcíon para actualizar el humor dependiendo del valor de nivel_felicidad
    def actualizar_humor(self):
        if self.nivel_felicidad >= 80:
            self.humor = "Eufórico"
        elif 50 <= self.nivel_felicidad < 80:
            self.humor = "Feliz"
        elif 20 <= self.nivel_felicidad < 50:
            self.humor = "Indiferente"
        elif 10 <= self.nivel_felicidad < 20:
            self.humor = "Triste"
        else:
            self.humor = "Enojado"

    #Función para limitar el valor que pueden tomar los valores (Mínimo 0 y Máximo 100)
    def actualizar_valores(self):
        self.nivel_energia = max(0, min(100, self.nivel_energia))
        self.nivel_hambre = max(0, min(100, self.nivel_hambre))
        self.nivel_felicidad = max(0, min(100, self.nivel_felicidad))
        
    #Funcion para bajar el hambre/energía periodicamente
    def pasoDelTiempo(self):
        while not bandera.is_set(): 
            self.nivel_hambre -= 1
            self.nivel_energia -= 1
            time.sleep(self.tiempo_de_espera)

    def iniciarTamagotchi(self):
        hilo_tamagotchi = threading.Thread(target=self.pasoDelTiempo)
        hilo_tamagotchi.daemon = True 
        hilo_tamagotchi.start()
        return hilo_tamagotchi