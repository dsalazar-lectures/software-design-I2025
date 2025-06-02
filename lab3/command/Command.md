# Laboratorio #3  
**Josué Torres Sibaja**  
**C37853**

## 1. Patrón Command

### 1.1. Definición del patrón y a qué tipo pertenece  
**Command** es un patrón de diseño **de comportamiento** que encapsula una solicitud (una acción) como un objeto, lo que permite parametrizar clientes con diferentes solicitudes, encolar o registrar solicitudes, y soportar operaciones como deshacer y rehacer.  
En términos simples, el patrón Command convierte una acción (como "crear review/calificar tutor") en un objeto independiente que puede ser almacenado, ejecutado, deshecho o combinado con otros comandos.

---

### 1.2. ¿Cuál es el problema común que resuelve?

Muchas veces en los sistemas es necesario:

- Ejecutar acciones que deben ser registradas o deshechas (como editar o eliminar una review).
- Mantener un bajo acoplamiento entre el objeto que invoca una operación (por ejemplo, el botón de "calificar tutor") y el objeto que realmente la realiza.
- Tratar operaciones como objetos reutilizables o configurables.

El patrón Command resuelve estos problemas al encapsular cada acción dentro de un objeto, separando **quién solicita la acción** de **quién la ejecuta**.

---

### 1.3. ¿Cómo mejora el mantenimiento o escalabilidad del sistema?

- **Bajo acoplamiento**: El cliente que lanza el comando no necesita conocer los detalles del receptor que lo ejecuta.
- **Extensibilidad**: Nuevas acciones se pueden agregar fácilmente implementando nuevos comandos, sin modificar el código existente.
- **Deshacer/Rehacer**: Como cada acción es un objeto, es posible almacenar su estado y revertirla si es necesario.
- **Macrocomandos**: Se pueden agrupar múltiples comandos y ejecutarlos como una sola unidad (por ejemplo, una review que incluya calificación + comentario).

Esto lo hace ideal para sistemas escalables donde las acciones del usuario (como en una página de tutorías) pueden cambiar, extenderse o requerir historial.

---

### 1.4. Otras ventajas y desventajas de su uso

#### 1.4.1. Ventajas

- Facilita la implementación de funcionalidades como **deshacer/rehacer**, **logs de acciones** y **colas de tareas**.
- **Desacopla** el emisor de la acción del receptor.
- Mejora la **modularidad y reutilización** del código.
- Puede facilitar la implementación de **comandos remotos**, **transacciones**, o ejecución **en diferido** (puede crear un comando ahora, pero ejecutarlo más tarde).

#### 1.4.2. Desventajas

- Introduce **mayor complejidad y número de clases**, ya que cada acción requiere su propia clase de comando.
- Si las acciones son muy simples, el patrón puede ser una **sobrecarga innecesaria**.
- Puede complicarse si no se maneja bien la **gestión de estados** para comandos reversibles.

---

## Referencias

- Refactoring.Guru. (s.f.). *Command*. https://refactoring.guru/es/design-patterns/command
- Blancarte, O. (s.f.). *Command*. Reactive Programming. https://reactiveprogramming.io/blog/es/patrones-de-diseno/command
- Leiva, A. (2023). *Command – Patrones de Diseño*. DevExpert. https://devexpert.io/command-patrones-diseno/
- Iluwatar. (s.f.). *Command*. Patrones De Diseño Java. https://java-design-patterns.com/es/patterns/command/#diagrama-de-clases