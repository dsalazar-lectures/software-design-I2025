# Arquitectura Hexagonal (Ports and Adapters)

## ¿Qué es?

"El patrón de **arquitectura hexagonal**, también conocido como patrón de puertos y adaptadores, fue propuesto por el **Dr. Alistair Cockburn** en 2005." Patrón de arquitectura hexagonal - AWS Guía prescriptiva. (2025). Amazon.com. 


## Objetivo

Separar claramente la lógica de negocio (core) de los mecanismos de entrada/salida (UI, DB, APIs), facilitando:
- La prueba de la lógica de negocio de forma independiente.
- La sustitución de tecnologías externas sin afectar el dominio.
- La adaptabilidad a nuevos canales de comunicación (web, CLI, APIs, etc.).

## Componentes clave
- **Núcleo de la aplicación (Core / Dominio):** Contiene la lógica de negocio pura.
- **Puertos:** Interfaces que definen lo que el sistema puede hacer (entrada) y lo que necesita de afuera (salida).
- **Adaptadores:** Implementaciones concretas de los puertos, que permiten la interacción con el núcleo de la aplicación.
- **aplicación:** Orquesta los casos de uso y coordina la interacción entre el núcleo y los adaptadores.
- **Infraestructura:** Implementaciones concretas de los adaptadores, como bases de datos, servicios externos, etc.


## Beneficios

- Independencia del framework
- Alta testabilidad
- Mejor mantenibilidad
- Facilidad para cambiar la infraestructura

## Ventajas frente a otras arquitecturas

- Independencia tecnológica
- Fácil de testear
- Adaptable a cambios

## Ejemplo en Python

- El dominio define un servicio `User`.
- Los puertos son interfaces: `UserRepository`.

El código está en la carpeta link [hexagonal_example](./hexagonal_example/)

# Fuentes:

- Salguero, E. (2018, June 22). Arquitectura Hexagonal - Edu Salguero - Medium. Medium. https://medium.com/@edusalguero/arquitectura-hexagonal-59834bb44b7f
- hdeleon.net [@hdeleonnet]. (s/f). ¿qué es arquitectura hexagonal? Youtube. Recuperado el 1 de junio de 2025, de https://www.youtube.com/watch?v=AnDDjeUFXSk
- Patrón de arquitectura hexagonal - AWS Guía prescriptiva. (2025). Amazon.com. https://docs.aws.amazon.com/es_es/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html#:~:text=El%20patr%C3%B3n%20de%20arquitectura%20hexagonal%20se%20utiliza%20para%20aislar%20la,datos%20o%20el%20c%C3%B3digo%20externo.
- García, M. A. [@mvrcoag]. (s/f). APRENDE ARQUITECTURA HEXAGONAL | cap. 1 domain. Youtube. Recuperado el 1 de junio de 2025, de https://www.youtube.com/watch?v=H0Sbna9rxog
- García, M. A. [@mvrcoag]. (s/f). APRENDE ARQUITECTURA HEXAGONAL | cap. 2 application. Youtube. Recuperado el 1 de junio de 2025, de https://www.youtube.com/watch?v=EcmRo9LUfyE
- García, M. A. [@mvrcoag]. (s/f). APRENDE ARQUITECTURA HEXAGONAL | cap. 1 infrastructure. Youtube. Recuperado el 1 de junio de 2025, de https://www.youtube.com/watch?v=np7nOWWZHtU