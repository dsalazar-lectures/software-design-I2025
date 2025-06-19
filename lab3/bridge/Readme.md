## Patrón Bridge

## Definición

El patrón **Bridge** es un patrón estructural que tiene como objetivo **desacoplar una abstracción de su implementación**, de modo que ambas puedan evolucionar de forma independiente. Es especialmente útil cuando se tienen múltiples variantes de una abstracción y sus implementaciones.

Corresponde a un patrón de tipo estructural, ya que se centran en cómo se organizan las clases y objetos para formar estructuras más grandes (otros ejemplos: Adapter, Bridge, Composite, Decorator).

> Cumple con el principio **Open/Closed**: abierto a extensión, cerrado a modificación, permitiendo agregar nuevos comportamientos sin cambiar el código existente.


## Caso de uso utilizado de ejemplo: 

**Situación**: Se quiere generar un informe, y puede hacerse en diferentes formatos: texto plano, HTML, PDF, etc.

-   El **contenido** del informe (nombre, email, etc.) es la **abstracción**.
    
-   El **formato** en que se presenta (HTML o texto plano) es la **implementación**.
    

Ambos pueden evolucionar por separado: puedes crear nuevos tipos de reportes o nuevos formatos de salida sin modificar los existentes. Esto se consigue utilizando el patrón Bridge. 

----------
## Problema común que resuelve

Evita una gran cantidad de combinaciones en clases cuando se cruzan múltiples dimensiones de variación. Por ejemplo:

-   `ReporteUsuarioTextoPlano`
    
-   `ReporteUsuarioHTML`
    
-   `ReporteFinanzasTextoPlano`
    
-   `ReporteFinanzasHTML`
    

Con Bridge, solo necesitas una jerarquía para el **tipo de reporte** y otra para el **formato de salida**, que pueden combinarse libremente.

## ¿Cómo mejora el mantenimiento o escalabilidad?

-   Permite agregar nuevos formatos o tipos de reportes sin modificar el código existente.
    
-   Favorece los principios SOLID, especialmente **Open/Closed Principle** y **Single Responsability Prinsiple**.
    
-   Separa claramente **qué** se genera del **cómo** se representa.
    
-   Reutiliza código común en las abstracciones.

## Ventajas

-   **Independencia** entre abstracción e implementación.
    
-   **Flexibilidad** para extender formatos o tipos de reporte.
    
-   **Reducción de duplicación**.
    
-   Facilita pruebas unitarias por separado.
    
----------

## Desventajas

-   Mayor complejidad inicial.
    
-   Puede ser innecesario para estructuras simples.
----------
## Ejemplo de uso en el proyecto

Se desarrolló una aplicación que permite generar reportes de usuario en distintos formatos. La aplicación define dos jerarquías:

1.  **Abstracción (`Report`)**: representa un tipo de reporte (en este caso, de usuario).
    
2.  **Implementación (`OutputFormat`)**: representa cómo se presenta ese reporte (texto plano o HTML).
    

### Componentes:

-   `Report`: clase abstracta que depende de una implementación de `OutputFormat`.
    
-   `UserReport`: un tipo de reporte concreto que contiene nombre y correo del usuario.
    
-   `PlainTextOutputFormat` y `HTMLOutputFormat`: dos maneras diferentes de representar el contenido del reporte.
    
# ¿En qué se diferencia Bridge de la herencia tradicional?

| Característica                                | Bridge                          | Herencia tradicional             |
|----------------------------------------------|----------------------------------|----------------------------------|
| Separación entre abstracción e implementación | Sí                               | No                               |
| Flexibilidad para combinar variantes          | Alta                             | Limitada                         |
| Composición vs Herencia                       | Composición (usa interfaces/clases) | Herencia directa              |
| Escalabilidad                                 | Alta (crecen jerarquías separadas) | Baja (clases combinadas)     |


# Diferencias con otros patrones estructurales

| Patrón       | Propósito principal                                | Diferencia con Bridge                                               |
|--------------|-----------------------------------------------------|----------------------------------------------------------------------|
| Bridge       | Separar una abstracción de su implementación        | Se enfoca en la independencia entre lo que se hace y cómo           |
| Adapter      | Adaptar una interfaz existente a otra esperada      | No separa abstracción, solo adapta interfaces                       |
| Decorator    | Agregar comportamiento sin modificar la clase original | No separa jerarquías; agrega funcionalidad dinámica             |
| Strategy (comportamiento) | Cambiar algoritmos en tiempo de ejecución      | Strategy cambia comportamientos, Bridge cambia implementaciones estructurales |

## Estructura del directorio

```plaintext
lab4/
└── bridge/
    ├── Main.java
    ├── Report.java
    ├── OutputFormat.java
    ├── PlainTextOutputFormat.java
    ├── HTMLOutputFormat.java
    └── UserReport.java
    └── FinanceReport.java

```

   
   ### Resultado de ejecución:

```text
=== Texto Plano ===
==== Reporte de Usuario ====
Nombre: Ana
Email: ana@email.com
```

```html
=== HTML ===
<h1>Reporte de Usuario</h1>
<p><strong>Nombre:</strong> Ana</p>
<p><strong>Email:</strong> ana@email.com</p>
```

## ¿Cómo se prueba el patrón Bridge?

La separación de responsabilidades permite probar cada componente por separado:

### Pruebas unitarias por componente

-   **Reportes**: se puede probar que generen contenido correctamente según los datos.
    
-   **Formatos**: se puede verificar que formatean adecuadamente título y líneas.
    

#### Ejemplo de prueba de formato HTML:
```java
@Test
public void testHTMLOutputFormat() {
    OutputFormat format = new HTMLOutputFormat();
    String title = format.formatTitle("Mi Título");
    assertEquals("<h1>Mi Título</h1>\n", title);
}

```
#### Ejemplo de prueba de Reporte:

```java
@Test
public void testUserReportPlainText() {
    OutputFormat format = new PlainTextOutputFormat();
    Report report = new UserReport(format, "Ana", "ana@email.com");

    String output = report.generate();
    assertTrue(output.contains("Nombre: Ana"));
}
```

## ¿Cómo ejecutar el ejemplo?

### Requisitos

-   Tener instalado **Java**
    
-   Un compilador (javac) y terminal configurada

- Contar con las siguientes librerías en el directorio lib:
  - [JUnit 4.13.2](https://search.maven.org/remotecontent?filepath=junit/junit/4.13.2/junit-4.13.2.jar)
  - [Hamcrest Core 1.3](https://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar)
  

### Pasos:

1.  Abrir una terminal en la carpeta del proyecto (`bridge/`)
    
2.  Compilar:
```bash
javac -cp "lib/*" -d bin src/*.java testing/*.java
```
3.  Ejecutar: 
```bash
java -cp bin src.Main
```

### Resultado esperado:

Verás los reportes generados en formato texto plano y HTML en la consola.


