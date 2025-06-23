## Definición y tipo
El **patrón Builder** es un patrón **creacional** que separa la construcción de un objeto complejo de su representación final. Mientras que el objeto (el “Producto”) oculta un constructor privado, un **Builder** expone una API fluida (*fluent interface*) con métodos `withXxx()` o `setXxx()` que van configurando paso a paso los distintos atributos. Sólo cuando se llama a `build()` se valida el estado y se devuelve el objeto totalmente inicializado e inmutable.

## Problema común que resuelve
- Cuando una clase tiene **muchos parámetros**, especialmente opcionales, usar **constructores telescópicos** (con docenas de sobrecargas) se vuelve inmantenible y poco legible.  
- Alternativas como setters pierden inmutabilidad y obligan al cliente a recordar un orden correcto de llamadas.  
- **Builder** ofrece una forma clara y segura de garantizar que:
  1. Todos los campos obligatorios queden definidos.  
  2. Los valores opcionales usen valores por defecto si no se configuran.  
  3. No exista objeto en estado inconsistente.  

## ¿Cómo mejora el mantenimiento y la escalabilidad?
- **Claridad en el cliente**: cada llamada `builder.withXxx(...)` nombra qué atributo se está configurando.  
- **Inmutabilidad del producto**: una vez construido, el objeto no cambia, reduciendo errores por estados mutables.  
- **Extensión sin romper**: para añadir un nuevo parámetro basta con crear un nuevo método `withNuevoParametro()` en el Builder; el código que usa el patrón no se ve afectado.  
- **Validaciones centralizadas**: en `build()` se hacen todas las comprobaciones (nulos, rangos, dependencias entre campos), evitando validaciones dispersas.  

## Otras ventajas
- **Reutilización de flujos**: se pueden definir varios “directores” o métodos estáticos que ensamblen configuraciones comunes (p. ej. `defaultProductionPipeline()`).  
- **Test Data Builder**: en pruebas, facilita la creación de objetos con valores por defecto que se pueden anular a conveniencia.  
- **API consistente**: todos los objetos complejos del dominio pueden seguir la misma convención de construcción.  
