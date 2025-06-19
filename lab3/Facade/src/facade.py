from devices import SensorTemperatura, ControlPersianas, AireAcondicionado, Iluminacion

class SmartHomeFacade:
    def __init__(self):
        self.sensor = SensorTemperatura()
        self.persianas = ControlPersianas()
        self.ac = AireAcondicionado()
        self.luces = Iluminacion()

    def activar_modo_verano(self):
        print("\nActivando Modo Verano...")
        self.sensor.encender()
        self.sensor.leer_temperatura_caliente()
        self.persianas.bajar()
        self.ac.encender()
        self.luces.luces_blancas()

    def activar_modo_invierno(self):
        print("\nActivando Modo Invierno...")
        self.sensor.encender()
        self.sensor.leer_temperatura_fria()
        self.persianas.subir()
        self.ac.apagar()
        self.luces.luces_calidas()
