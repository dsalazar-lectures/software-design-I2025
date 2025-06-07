class SensorTemperatura:
    def encender(self):
        print("Sensor de temperatura activado.")
        
    def leer_temperatura_fria(self):
        print("Temperatura actual: 15°C.")

    def leer_temperatura_caliente(self):
        print("Temperatura actual: 30°C.")

class ControlPersianas:
    def bajar(self):
        print("Persianas abajo para no dejar entrar luz.")

    def subir(self):
        print("Persianas arriba para dejar entrar luz.")

class AireAcondicionado:
    def encender(self):
        print("Aire acondicionado encendido.")

    def apagar(self):
        print("Aire acondicionado apagado.")

class Iluminacion:
    def luces_calidas(self):
        print("Luces cálidas encendidas para ambientar la habitación.")

    def luces_blancas(self):
        print("Luces blancas encendidas para mayor visibilidad.")
