# Patrón Repository con DTOs

## Que es un DTO?

Un **DTO (Data Transfer Object)** es un patrón de diseño utilizado para transferir datos entre diferentes capas de una aplicación mientras:

- Desacopla el modelo de dominio de los detalles de persistencia
- Optimiza los formatos de transferencia de datos
- Proporciona un contrato claro entre capas

## Importancia de los DTOs

1. **Aislamiento de capas**  
   Previene que los esquemas de base de datos "contaminen" la lógica de negocio

2. **Control de seguridad**  
   Expone solo los datos necesarios (evita enviar campos sensibles)

3. **Optimización de rendimiento**  
   Permite moldear datos específicamente para cada caso de uso

4. **Soporte para versionado**  
   Facilita la compatibilidad hacia atrás cuando las APIs evolucionan

## Problemas que resuelven los DTOs

| Problema                                                 | Solución                                        |
| -------------------------------------------------------- | ----------------------------------------------- |
| Cambios en esquemas de BD afectan al dominio             | Los DTOs absorben los cambios de persistencia   |
| Obtención excesiva de datos desde bases de datos         | Los DTOs seleccionan solo los campos necesarios |
| Diferentes clientes necesitan diferentes formas de datos | Multiples DTOs por entidad                      |
| Objetos de dominio contienen lógica de persistencia      | Los DTOs manejan el formato de almacenamiento   |

## Cuando usar este patrón

- Integración con APIs externas
- Soporte para múltiples bases de datos
- Construcción de microservicios
- Versionado de contratos de API

## Cuando evitar su uso

- Aplicaciones CRUD extremadamente simples
- Prototipos/POCs sin necesidades de mantenimiento a largo plazo
- Secciones críticas de rendimiento donde la sobrecarga de mapeo es importante

## Como ejecutar el ejemplo

1. Clonar el repositorio
2. Abrir en Visual Studio
3. Ejecutar `Program.cs` para ver ambas implementaciones de repositorio en acción en VS o corriendo `dotnet run`