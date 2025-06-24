# Observer Pattern – Temperature Sensor Demo

Este proyecto es una implementación del **Patrón de Diseño Observador** en C#, siguiendo una arquitectura tipo MVC para simular el comportamiento de un sensor de temperatura que notifica a múltiples observadores cuando hay un cambio.

## ¿Qué hace este programa?

El programa simula un **sensor de temperatura** que registra valores ingresados por el usuario. Cada vez que se actualiza la temperatura, se notifica automáticamente a todos los observadores registrados:

- **Display**: muestra la temperatura en consola.
- **Alarm**: lanza una advertencia si la temperatura supera cierto umbral (ej. 30°C).
- **Logger**: registra la temperatura.

Este patrón permite mantener una arquitectura **desacoplada**, donde el sujeto (sensor) no necesita saber quién lo observa ni cómo reaccionan él nada mas les notifica.

## ¿Cómo compilar y ejecutar?

### Requisitos:
- [.NET SDK 6.0+](https://dotnet.microsoft.com/en-us/download)

### 🔧 Pasos para compilar:

1. Abrí una terminal en la raíz del proyecto:

```bash
cd path/to/ObserverDemo
```

2. Compilamos el proyecto:

```bash
dotnet build
```

3. Ejecutá la aplicación:

```bash
dotnet run
```

4. El programa funciona ingresando temperaturas de forma manual:

```text
Enter a new temperature (or 'exit'): 28
[Pantalla] Temperatura actual: 28°C
[Logger] Temperature recorded: 28°C

Enter a new temperature (or 'exit'): 45
[Pantalla] Temperatura actual: 45°C
[Alarm] High temperature detected!
[Logger] Temperature recorded: 45°C
```

5. Para salir del programa solo es necesario escribir `exit` o `salir`.
