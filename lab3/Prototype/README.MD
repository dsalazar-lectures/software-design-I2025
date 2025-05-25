# Patrón: Prototype
### Definición del patrón y a qué tipo pertenece

El Patrón Prototype es un patrón creacional que permite crear nuevos objetos mediante la copia (clonado) de un objeto existente, llamado prototipo, en lugar de instanciarlos directamente.

Este patrón es útil cuando la creación de objetos es costosa en términos de recursos o complejidad. La idea central es definir una interfaz con un método clone(), que cada clase concreta implementará según sus necesidades.

   

### ¿Cuál es el problema común que resuelve?

Durante el desarrollo de software es común necesitar:

- Crear objetos complejos o costosos de inicializar.
- Instanciar clases sin conocer su clase concreta exacta (por ejemplo, cuando se trabaja con interfaces o clases base).
- Evitar la duplicación de código al construir objetos similares.

El patrón Prototype resuelve esto al permitir la creación de objetos mediante la clonación de un objeto ya configurado, evitando así inicializaciones repetidas y dependencias a clases concretas.

### ¿Cómo mejora el mantenimiento o escalabilidad del sistema?

- Reduce el acoplamiento: ya que no se depende de clases concretas para crear objetos. *(Mantenimiento)*

- Aumenta la flexibilidad: nuevos tipos de objetos se pueden agregar fácilmente sin modificar el código cliente. *(Escalabilidad)*

- Evita código repetido: permite reutilizar la configuración de un prototipo para generar otros objetos similares. *(Mantenimiento)*

- Facilita la creación de objetos complejos: al clonar un prototipo ya configurado. *(Escalabilidad)*

### Otras ventajas

- Puedes clonar objetos sin acoplarlos a sus clases concretas.

- Evita código de inicialización repetitivo al reutilizar prototipos prefabricados.

- Ideal para sistemas donde se crean muchas instancias similares.

### Desventajas

Clonar objetos complejos con referencias circulares puede ser complicado.
Ejemplos típicos:

- Amigos en una red social (referencias mutuas).

- Árboles donde padres e hijos se referencian mutuamente.

- Listas circulares.

En lenguajes como C++, donde el manejo de memoria es manual, estos ciclos pueden provocar:

- Fugas de memoria si no se usan destructores apropiados o punteros inteligentes.

- Ciclos infinitos si el clonado no controla objetos ya copiados.

### Posibles soluciones:

- Usar punteros inteligentes (shared_ptr y weak_ptr) para evitar ciclos fuertes.

- Usar estructuras auxiliares (como mapas) para registrar objetos ya clonados.

- Serializar objetos como alternativa al clonado profundo directo.

## Ejemplo de aplicación del patrón Prototype en una página de tutorías

Supongamos que estamos desarrollando una página de tutorías donde los estudiantes pueden buscar tutores para diferentes materias. En este caso, podríamos usar el patrón Prototype para clonar objetos de tutor configurados previamente, en lugar de crear nuevos objetos desde cero cada vez.

### Escenario

En la página de tutorías, cada tutor tiene un perfil que incluye información como:
- Nombre
- Materia(s) que enseña
- Disponibilidad
- Tarifa por hora

En lugar de crear un nuevo objeto Tutor para cada solicitud, podemos tener prototipos preconfigurados para tutores de diferentes materias y clonar estos prototipos según sea necesario.

### Implementación

```python
from copy import deepcopy

class TutorPrototype:
    def __init__(self, name, subjects, availability, hourly_rate):
        self.name = name
        self.subjects = subjects
        self.availability = availability
        self.hourly_rate = hourly_rate

    def clone(self):
        return deepcopy(self)

# Crear prototipos de tutores
math_tutor_prototype = TutorPrototype("Tutor de Matemáticas", ["Álgebra", "Cálculo"], "Lunes a Viernes", 20)
science_tutor_prototype = TutorPrototype("Tutor de Ciencias", ["Física", "Química"], "Fines de Semana", 25)

# Clonar un tutor de matemáticas para un estudiante
student_tutor = math_tutor_prototype.clone()
student_tutor.name = "Juan Pérez"
student_tutor.availability = "Martes y Jueves"

print(f"Tutor asignado: {student_tutor.name}, Materias: {student_tutor.subjects}, Disponibilidad: {student_tutor.availability}, Tarifa: ${student_tutor.hourly_rate}/hora")
```

### Ventajas
- **Escalabilidad**: Podemos agregar nuevos prototipos para diferentes materias sin modificar el código existente.
- **Mantenimiento**: Evitamos duplicar código al reutilizar prototipos preconfigurados.

Este enfoque es especialmente útil en sistemas donde se crean muchas instancias similares, como perfiles de tutores en una página de tutorías.

## Aplicación del patrón Prototype en la creación de tutorías

En el contexto de la creación de tutorías, podemos usar el patrón Prototype para clonar tutorías preconfiguradas en lugar de crearlas desde cero cada vez. Esto es útil cuando las tutorías tienen configuraciones similares, como el método (virtual o presencial), la capacidad, o el formato general.

### Implementación

```python
from copy import deepcopy

class Tutorial:
    def __init__(self, id, title, tutor_id, tutor, subject, date, start_time, description, method, capacity, student_list=None):
        self.id = id
        self.title = title
        self.tutor_id = tutor_id
        self.tutor = tutor
        self.subject = subject
        self.date = date
        self.start_time = start_time
        self.description = description
        self.method = method
        self.capacity = capacity
        self.student_list = student_list or []

    def clone(self):
        return deepcopy(self)

# Crear prototipos de tutorías
virtual_tutorial_prototype = Tutorial(0, "", 0, "", "", "", "", "", "Virtual", 10)
presential_tutorial_prototype = Tutorial(0, "", 0, "", "", "", "", "", "Presencial", 20)

# Clonar una tutoría virtual para un caso específico
new_tutorial = virtual_tutorial_prototype.clone()
new_tutorial.id = 4
new_tutorial.title = "Tutoria de Python"
new_tutorial.tutor_id = 3
new_tutorial.tutor = "Laura Méndez"
new_tutorial.subject = "Programación III"
new_tutorial.date = "2025-10-10"
new_tutorial.start_time = "15:00"
new_tutorial.description = "Reforzar conceptos avanzados de Python"

print(f"Nueva tutoría creada: {new_tutorial.title}, Tutor: {new_tutorial.tutor}, Método: {new_tutorial.method}, Capacidad: {new_tutorial.capacity}")
```

### Ventajas
- **Escalabilidad**: Permite agregar nuevos prototipos para diferentes tipos de tutorías sin modificar el código existente.
- **Mantenimiento**: Evita duplicar código al reutilizar prototipos preconfigurados.

Este enfoque es especialmente útil en sistemas donde se crean muchas instancias similares, como las tutorías en una plataforma educativa.

 ### Bibliografía 
 Geoks for Geeks. (2025). Prototype Design Pattern. https://www.geeksforgeeks.org/prototype-design-pattern/ 
 Shvets A. (2021). Sumérgete en los patrones de diseño.