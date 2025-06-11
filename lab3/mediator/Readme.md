# Patrón Mediator

## Laboratorio 3: Patrones de Diseño de Software

C15464 Werner Naranjo Navarro – Diseño de Software


## Definición

El patrón **Mediator** es un **patrón de comportamiento** que define un objeto, comúnmente denominado *mediador*, que encapsula y gestiona el cómo interactúan un conjunto de objetos o componentes. En vez de que los componentes se comuniquen entre sí, el mediador funciona como punto medio entre estos. Gracias a esto, se evitan las referencias cruzadas entre objetos, promoviendo así el **desacoplamiento**.

Este patrón es útil cuando un sistema posee una gran variedad de objetos que deben interactuar entre sí de forma compleja. La clase mediadora no solo funciona como organizadora para mejora el flujo de la interacción, sino que también hace el código modularizable, y fácil de modificar y/o extender.

> El Mediator centraliza la comunicación entre objetos, siguiendo el principio de **bajo acoplamiento**.


## ¿Qué problema resuelve?

En sistemas donde múltiples objetos se comunican entre sí directamente, como botones, listas o cuadros de texto en una UI, es bastante común que se generen dependencias circulares, referencias cruzadas e interconexiones díficiles de rastrar, mantener y escalar.

Conforme más componentes son añadidos a la interfaz, estas dependencias aumentan exponencialmente, provocando fragilidad y haciendo dificil entender y modificar el código.

El patrón Mediator resuelve este problema al:
- Evitar que los objetos conozcan detalles internos de otros objetos.
- Centralizar las reglas de interacción en un único punto.
- Eliminar dependencias directas entre componentes.

## ¿Cómo mejora el mantenimiento o la escalabilidad?

- **Mantenimiento**  
  Este patrón mejora el mantenimiento al centralizar la lógica de interacción, los componentes individuales son más simples y enfocados en sus propias responsabilidades. Cambiar una interacción no implica modificar todos los objetos implicados.

- **Escalabilidad**  
  Se pueden agregar nuevos componentes o modificar los existentes sin tener que alterar el resto del sistema. Solo es necesario ajustar la lógica en el Mediator.

## Ventajas

- Disminuye el acoplamiento entre componentes.  
- Mejora la legibilidad y organización del flujo de interacción.  
- Favorece los principios SOLID, especialmente el **Single Responsibility Principle (SRP)** y **Open/Closed Principle (OCP)**.  
- Facilita la reutilización de componentes en diferentes contextos.  

## Desventajas

- El Mediator puede volverse una clase muy compleja si maneja demasiadas interacciones.  
- Puede ocultar la lógica de negocio si no se organiza adecuadamente.  
- Riesgo de sobreuso cuando no se requiere coordinación compleja.

## Ejemplo práctico

Para ilustrar el uso del patrón Mediator, se desarrolló una aplicación compuesta por:

- Un frontend en **React** que contiene tres componentes: un campo de texto, un botón y una etiqueta de mensaje.
- Un backend en **Flask (Python)** que simula el procesamiento del formulario y responde con mensajes de éxito o error.
- Un objeto **Mediador** en el frontend que centraliza toda la interacción entre componentes, evitando que se comuniquen directamente entre sí.

### ¿Cómo funciona?

1. El usuario escribe su nombre en un campo de texto.
2. El botón "Enviar" se activa solo si el campo contiene texto.
3. Al presionar el botón, se envía el nombre al servidor Flask mediante `fetch`.
4. El backend responde con un mensaje de confirmación o error.
5. Todos los componentes se comunican a través de un objeto central `FormularioMediator`.

Este enfoque demuestra cómo el patrón Mediator puede aplicarse eficazmente a interfaces gráficas desacoplando los componentes visuales y lógicos.

## ¿Cómo ejecutar la aplicación?

### 1. Prerequisitos

- Tener instalado **Python 3** y **Node.js + npm**
- Dentro de directorio raíz del patrón `.\mediator` cree un entorno virtual
```bash
python -m venv venv
```

- Active el entorno virtual
```bash
venv\Scripts\activate
```

- Instale las dependencias
```bash
pip install -r requirements.txt
```

- **Cuando desee terminar la prueba**, para desactivar el entorno virtual, ejecute:
```bash
deactivate
```

### 2. Compilar el backend

- Correr la app
```bash
python app.py
```

### 3. Compilar el frontend

- Abrir una nueva terminal
- Desde la carpeta `.\frontend`:
```bash
npm start
```
Esto abrirá la aplicación en http://localhost:3000.

