# Realizo los siguientes imports ya que me ayudan a simular el delay de los intentos 
import time
import random

def servicio_de_pago_magico():
    # En este método quiero simular una API de pago como paypal, bitcoin, sinpe... etc es mágico
    # asigno una probabilidad aleatoria de que el servicio falle
    if(random.random() < 0.4):
        # informamos de que no nos pudimos conectar con el servidor
        # indicamos la excepción Connection Error
        raise ConnectionError("Fallo temporal intento conectarse al servidor del método de pago\n")
    else:
        return("Pago realizado con éxito")
    
def sim_compra_item():
    #Definimos el número del intentos realizados
    intentos = 0
    #Definimos la cantidad máxima de intentos antes de botar el programa
    #En este caso pusimos 5
    max_reintentos = 5
    #Definimos el tiempo de delay inicial
    delay = 1
    #Definimos el backoff que es el timepo exponencial que incrementa el delay luego de cada intento fallido
    backoff = 2
    while intentos < max_reintentos:
        try:
            return servicio_de_pago_magico()
        except Exception as e:
            # Aumentamos la cantidad de intentos realizados 
            intentos += 1
            print("Intento fallido\n")
            print(f"Intento {intentos} fallido: {e}. Reintentando en {delay} segundos...")
            # Simulamos el delay para volver a hacer un nuevo intento 
            time.sleep(delay)
            # Aumentamos el delay de manera exponencial
            delay *= backoff
    
    raise Exception("Todos los intentos que realizamos fallaron\n")
    

print(sim_compra_item())