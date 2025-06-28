# Patrón Facade – Diseño de Software
## Laboratorio 3
* **Nombre:** Isabella Rodríguez Sánchez
* **Carnet:** C26701


## Definición

El patrón **Facade** es un patrón de diseño estructural que proporciona una interfaz unificada para un conjunto de interfaces en un subsistema. Facade define una interfaz de más alto nivel que hace el subsistema más fácil de usar para los clientes.

> "The Facade pattern defines a higher-level interface that makes the subsystem easier to use."  
> — *Gamma et al., Design Patterns: Elements of Reusable Object-Oriented Software, 1994*

🔹 Tipo de patrón: **Estructural**  
🔹 Propósito: **Simplificar el acceso a sistemas complejos**

---

## Problema que resuelve

En sistemas grandes, los clientes deben interactuar con múltiples clases o componentes que pueden ser complejos o estar altamente acoplados. Esto aumenta la dificultad de mantenimiento, uso y prueba del sistema.

El patrón Facade actúa como una API simplificada que agrupa operaciones internas en un conjunto reducido de métodos de alto nivel. Así el cliente interactúa con un solo punto de entrada, sin necesidad de conocer los detalles del sistema.

- **Separación de responsabilidades:** el cliente no tiene que coordinar pasos complejos.
- **Abstracción limpia:** el sistema puede cambiar por dentro sin afectar al consumidor.
- **Mejora del principio de inversión de dependencias:** el cliente depende de una abstracción (el Facade), no de múltiples clases concretas.

---

##  ¿Cómo mejora el mantenimiento y escalabilidad?

### Mantenimiento
El patrón permite que los componentes internos del subsistema cambien sin afectar a los clientes, siempre que la interfaz del facade se mantenga.

### Escalabilidad
Permite agregar nuevas funcionalidades al subsistema sin que el cliente tenga que conocerlas directamente. Se puede extender el facade o crear nuevos métodos de acceso.


---

## Ventajas

- **Reduce el acoplamiento:**
El cliente solo depende de la fachada, no de múltiples clases internas.
- **Simplifica el uso del sistema:**
Proporciona una API de alto nivel fácil de entender y usar.
- **Facilita el mantenimiento y escalabilidad:**
Los cambios en los subsistemas no afectan al cliente y permite añadir nuevas funcionalidades fácilmente.
- **Mejora la organización modular:**
Separa la lógica de coordinación u organización de los detalles de implementación.
- **Favorece la testabilidad:**
Permite probar la lógica principal desde un solo punto de acceso.

## Desventajas

- **Oculta funcionalidades avanzadas:**
Puede limitar el acceso a operaciones específicas del subsistema.
- **Riesgo de sobrecarga:**
Una fachada mal diseñada puede asumir demasiadas responsabilidades y volverse inflexible.
- **Sensación falsa de simplicidad:**
Puede ocultar la complejidad real del sistema para desarrolladores nuevos.
- **Agrega una capa adicional:**
En sistemas simples, puede ser innecesario y aumentar la complejidad sin beneficio.
---

##  Ejemplo – Sistema de Casa Inteligente (Smart Home)

Se desarrolló un sistema de casa inteligente en Python, que simula distintos dispositivos controlables mediante una única interfaz de alto nivel.


###  Subsistemas

- `SensorTemperatura`: simula sensores de temperatura.
- `ControlPersianas`: controla el estado de persianas (subir/bajar).
- `AireAcondicionado`: activa o apaga el sistema de aire.
- `Iluminacion`: cambia entre luces cálidas y luces blancas.

Cada uno representa un componente interno que puede ser complejo o con múltiples interacciones.

---

###  Clase `SmartHomeFacade`

```python
class SmartHomeFacade:
    def activar_modo_verano(self):
        # Activa sensores, baja persianas, enciende aire, luces blancas
        ...

    def activar_modo_invierno(self):
        # Activa sensores, sube persianas, apaga aire, luces cálidas
        ...
```

La clase facade orquesta la interacción de los componentes internos y ofrece una interfaz sencilla con dos métodos:
- `activar_modo_verano()`
- `activar_modo_invierno()`
---

###  Código Cliente (`main.py`)

```python
from facade import SmartHomeFacade

def main():
    casa = SmartHomeFacade()
    casa.activar_modo_verano()
    casa.activar_modo_invierno()
```

El cliente solo necesita conocer la fachada para controlar todo el sistema.

---

##  Conclusión

El patrón Facade es uno de los más usados en la ingeniería de software porque simplifica la interacción con sistemas complejos. De hecho, muchos lo usamos a diario sin saberlo, en librerías, frameworks o APIs, lo que vuelve más accesible herramientas importantes, como Flask en el proyecto

---

##  Fuentes

- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
- Khomh, F., Gueheneuc, Y. G., & Antoniol, G. (2009). *Playing roles in design patterns: An empirical descriptive and analytic study*. Empirical Software Engineering.
- Freeman, E., Freeman, E., Bates, B., & Sierra, K. (2004). *Head First Design Patterns*. O’Reilly Media.