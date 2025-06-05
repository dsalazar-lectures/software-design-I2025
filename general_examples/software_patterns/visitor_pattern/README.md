# Patrón de Diseño: Visitor

## ¿Qué es el patrón Visitor?

El patrón **Visitor** permite separar algoritmos de los objetos sobre los que operan. Es un patrón de comportamiento que permite agregar nuevas operaciones a objetos sin modificar sus clases. 

Este patrón introduce un visitante externo que realiza una operación en una colección de objetos con diferentes clases, pero que comparten una interfaz común.

---

## ¿Cuándo usar Visitor?

- Cuando quieres agregar nuevas operaciones a una jerarquía de clases sin modificarlas.
- Cuando una operación involucra objetos de distintas clases y necesitas realizar acciones distintas para cada una.
- Cuando quieres centralizar la lógica de una operación sin dispersarla por toda la jerarquía de clases.

---

## Ventajas

- **Separación de responsabilidades**: Las operaciones se separan de los objetos que las contienen.
- **Fácil de extender**: Puedes agregar nuevas operaciones sin modificar las clases base.
- **Centralización de lógica**: Toda la lógica relacionada con una operación específica está en un solo lugar.

---

## Desventajas

- **Difícil de mantener si cambian las estructuras**: Agregar nuevas clases a la jerarquía de elementos obliga a modificar todos los visitantes.
- **Puede ser verboso**: Requiere escribir una clase visitante con métodos para cada tipo de elemento.

---

## ¿Cómo mejora el código?

Este patrón evita violar el Principio de Abierto/Cerrado. Por ejemplo, si necesitas ejecutar nuevas operaciones sobre objetos `Car`, `Bike`, `Truck`, puedes hacerlo sin modificar sus clases directamente, simplemente creando un nuevo visitante.