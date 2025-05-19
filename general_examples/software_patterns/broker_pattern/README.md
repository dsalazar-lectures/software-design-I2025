# Patrón Broker

## ¿Qué es el Patrón Broker?

El patrón **Broker** es un patrón de diseño arquitectónico que permite **desacoplar clientes y servicios** mediante un componente intermediario llamado *broker*. Este patrón se utiliza cuando los objetos que realizan solicitudes no necesitan saber dónde o cómo se implementan los servicios que satisfacen esas solicitudes.

En lugar de comunicarse directamente, los clientes envían peticiones al broker, y este se encarga de enrutar, coordinar o reenviar las solicitudes al servicio adecuado.

## ¿Cuándo se utiliza?

- En sistemas distribuidos o basados en microservicios.
- Cuando se desea **desacoplar** completamente al cliente de los servicios.
- Cuando se necesita **soporte para múltiples servicios** con interfaces heterogéneas.
- Para facilitar la integración con protocolos distintos.

## Componentes principales

1. **Cliente (Client):** Solicita una operación o servicio.
2. **Broker:** Intermediario que enruta las solicitudes del cliente a los servicios adecuados.
3. **Servicio (Server):** Proveedor de operaciones concretas.

## Ventajas

- Permite la escalabilidad del sistema mediante desacoplamiento.
- Mejora la mantenibilidad y extensibilidad del sistema.
- Permite ocultar detalles de implementación y localización de los servicios.

## Desventajas

- Agrega complejidad adicional al sistema.
- Puede convertirse en un cuello de botella si no se gestiona correctamente.
- Mayor dificultad para depurar y monitorear.