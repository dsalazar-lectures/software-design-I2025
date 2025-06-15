# Lab#3 Diego Cerdas Delgado C21988

# Retry

# ¿Qué es el patrón Retry?

## El patrón Retry es un patrón de diseño de resiliencia que automatiza la reintención (retry) de una operación que puede fallar temporalmente, con el objetivo de dar más oportunidades a que se complete exitosamente.

# Aplicaciones de Retry

- Conexiones de red.
- Consultas a APIs externas.
- Lectura/escritura en bases de datos.
- Servicios remotos.

# Importancia

- Las fallas temporales son comunes (timeouts, caídas parciales, concurrencia).
- Retry ayuda a mejorar la tolerancia a fallos de un sistema, sin intervención manual.
- Reduce la necesidad de que el usuario reintente manualmente una operación.

# Conceptos clave

- Número máximo de intentos.
- Delay entre cada intento.
- Incremento exponencial en el delay luego de cada error.
- Jitter.(concepto que vemos en el curso de redes)

# Ventajas
- Mejora la resilencia del sistema. 
- Reduce el impacto de los errores temporales.
- Automatiza lógica repetitiva que el usuario o desarrollador tendría que hacer manualemnte.(Como refrescar la ventana en la web)

# Desventajas
- Si no se aplica bien puede producir sobrecarga en el sistema remoto
- No resuelve fallos permanentes, solo espera por respuestas exitosas.
- Puede aumentar los tiempos de respuesta.

# ¿Cuando aplicar este patrón?
 - Cuando sabemos que los fallos son intermitentes o transitorios.
 - En operaciones críticas, como pagos o consultas esenciales.

# ¿Cuando no aplicar este patrón?
- En errores permanentes e inmutables
- Cuando repetir una operación puede duplicación o inconsistencia.