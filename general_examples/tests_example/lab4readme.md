# Laboratorio 4 - Pruebas Unitarias y CI/CD

**Nombre:** Isabella Rodríguez Sánchez

**Carnet:** C26701


### Artefacto nuevo: `MicrowaveArtifact`

Se implementó la clase `MicrowaveArtifact` que extiende `ICookingArtifact`. A diferencia de otros artefactos como el horno o el air fryer, el microondas tiene estas funcinalidades:

- Si el tiempo de cocción es mayor a 60 minutos, el estado pasa a "error".
- Si es menor a 3 minutos, el estado es "warming".
- En otros casos, el estado es "cooked".

Este diseño permite validar distintos flujos de ejecución y estados, siguiendo el principio de sustitución de Liskov y favoreciendo el polimorfismo.

---

### Servicio nuevo: `MicrowaveCookingService`

Se implementó un nuevo servicio `MicrowaveCookingService`, siguiendo la interfaz `ICookingService`, y utilizando inyección de dependencias con la clase `Recipe`.

Este servicio:

- Cocina todos los artefactos con cook_all(minutes).
- Luego obtiene los estados y si alguno tiene el estado "error", devuelve un mensaje de fallo (por el microwave artifact que puede tirar error).
- Si no hay errores, devuelve un mensaje de éxito con los minutos utilizados.

Esta lógica muestra cómo los servicios pueden tomar decisiones basadas en los estados de los artefactos, usando el principio de inversión de dependencias.

---

### Pruebas realizadas

Se implementaron las siguientes pruebas:

- **Artefacto `MicrowaveArtifact`**:
  - Cocción normal (estado cooked)
  - Tiempo corto (estado warming)
  - Tiempo excesivo (estado error)

- **Servicio `MicrowaveCookingService`**:
  - Verifica respuesta correcta si todo está bien.
  - Reporta correctamente el estado de los artefactos.
  - Detecta errores si se cocinó demasiado tiempo.

Estas pruebas siguen buenas prácticas de unit testing y están aisladas entre sí.

![alt text](image.png)
---

### CI/CD Pipeline con GitHub Actions

En un entorno profesional, es común automatizar la ejecución de pruebas y validaciones cada vez que se hace un cambio en el repositorio, especialmente en proyectos que son colaborativos. Esto se logra mediante un pipeline CI/CD (Integración Continua / Entrega Continua).

En este lab se configuró un pipeline simple usando GitHub Actions. Este pipeline:

- Se activa automáticamente al hacer un push o pull request hacia la rama main.
- Crea un entorno virtual y configura Python.
- Instala las dependencias desde requirements.txt.
- Ejecuta los tests definidos con pytest.

Este archivo se encuentra en:
`.github/workflows/python-tests.yml`

---

### Buenas prácticas aplicadas

- Principios SOLID (especialmente Inversión de Dependencias y Abierto/Cerrado).

- Inyección de dependencias.

- Uso de interfaces para permitir mocks y testeo desacoplado.

- Tests unitarios claros, repetibles y relevantes.

- Pipeline CI/CD