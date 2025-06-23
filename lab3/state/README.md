# Patrón State
**Tipo**: Patrón de Comportamiento  
**Caso de Uso en el Proyecto**: Gestión de estados de pedidos en un sistema de e-commerce ("Pendiente", "Enviado", "Entregado", "Cancelado").

## Definición del Patrón
Patrón que permite a un objeto alterar su comportamiento cuando su estado interno cambia. Cada estado se encapsula en una clase independiente.

## Problema Común que Resuelve
- Elimina condicionales complejos (if/switch) al manejar transiciones entre estados.

- Evita código repetido en operaciones sensibles al estado del objeto.

## Beneficios
**Mantenimiento**:  
  - Añadir nuevos estados no requiere modificar el contexto principal  
  - Cada estado tiene responsabilidad única (SOLID)  

**Escalabilidad**:  
  - Transiciones claras y centralizadas  
  - Fácil extensión para nuevos comportamientos  

## Ventajas y Desventajas
| Ventajas                         | Desventajas                                     |
|----------------------------------|-------------------------------------------------|
| Código más organizado            | Sobrecarga de clases                            |
| Cumple con Open/Closed Principle | Complejidad inicial                             |
| Facilita testing unitario        | No es necesario para máquinas de estado simples |
