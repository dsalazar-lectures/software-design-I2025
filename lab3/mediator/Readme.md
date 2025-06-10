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