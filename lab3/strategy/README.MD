# Patrón Strategy

## Laboratorio 3: Patrones de Diseño de Software

Tatiana Paramo – Diseño de Software – 2025

## Definición

El patrón **Strategy** es un **patrón de comportamiento** que permite definir una familia de algoritmos, encapsular cada uno y hacerlos intercambiables. Este patrón permite que el algoritmo varíe independientemente del cliente que lo utiliza.

> Cumple con el principio **Open/Closed**: el sistema es abierto a la extensión, pero cerrado a la modificación.

---

## Analogía del mundo real

**Situación:** Estás en el supermercado y decides cómo pagar tus compras.

Opciones de pago (estrategias):
- Tarjeta
- Efectivo
- Pago móvil (Sinpe, Apple Pay, etc.)

Aunque el objetivo (pagar) es el mismo, cada método tiene su propio algoritmo. Como cliente, simplemente eliges el método y el sistema se encarga del resto.

Esto representa perfectamente el patrón Strategy: cada método de pago es una estrategia intercambiable que cumple una interfaz común (pagar).

---

## Problema que resuelve

Evita el uso excesivo de estructuras condicionales (`if-else`, `switch`) al momento de tomar decisiones que dependen del comportamiento. En su lugar, delega esas decisiones a clases concretas que implementan una estrategia específica.

---

## ¿Cómo mejora el mantenimiento o escalabilidad?

- Permite agregar nuevas estrategias sin modificar el código existente.
- Reduce el acoplamiento entre clases.
- Facilita la prueba de cada estrategia por separado.
- Mejora la organización y legibilidad del código.
- Favorece los principios SOLID, especialmente SRP y OCP.

---

## Ventajas

- Intercambiabilidad de algoritmos en tiempo de ejecución.
- Código más limpio y modular.
- Mejor mantenibilidad y escalabilidad.
- Pruebas unitarias más sencillas.

---

## Desventajas

- Puede generar muchas clases.
- Aumenta la complejidad inicial.
- Sobreingeniería en problemas simples.

---

## ¿En qué se diferencia Strategy de la herencia tradicional?

| Característica                                | **Strategy**                                               | **Herencia tradicional**                            |
| --------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------- |
| Cambiar comportamiento en tiempo de ejecución | Sí                                                         |   No, el comportamiento está fijo en la clase base  |
| Composición vs. Herencia                      | **Composición** : se inyecta el algoritmo como objeto    |  **Herencia**: sobrescritura de métodos             |
| Flexibilidad                                  | Alta: puedes cambiar el algoritmo sin modificar clases     | Baja: requiere modificar o extender clases          |
| Reutilización de código                       | Alta: estrategias son independientes y reutilizables       | Limitada por la jerarquía de clases                 |
| Acoplamiento                                  | Bajo: el cliente depende solo de la interfaz de estrategia | Alto: las subclases dependen de la clase base       |


## Diferencias entre Strategy y otros patrones de comportamiento

| Patrón             | ¿Cuál es su propósito?                                                                 | ¿Cómo se diferencia del patrón Strategy?                                                                 |
|--------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **Strategy**        | Permite seleccionar entre múltiples algoritmos intercambiables                         | Encapsula algoritmos completos y permite cambiarlos dinámicamente mediante composición                   |
| **Decorator**       | Añade responsabilidades a un objeto dinámicamente sin alterar su clase                 | Se enfoca en **extender funcionalidad**, no en seleccionar algoritmos completos como Strategy             |
| **Template Method** | Define el esqueleto de un algoritmo en una clase base y deja que las subclases lo completen | Usa **herencia**, no composición. El algoritmo base es fijo y solo se modifican partes específicas        |
| **State**           | Permite cambiar el comportamiento de un objeto cuando su estado interno cambia         | Similar estructura, pero el foco está en **cambiar estados internos**, no en elegir algoritmos            |
| **Command**         | Encapsula una acción como un objeto, útil para operaciones reversibles y encoladas     | Strategy encapsula **cómo hacer algo** (algoritmo); Command encapsula **qué hacer** (acción)              |

---

## Ejemplo de uso en el proyecto

Se realizó una aplicación donde los usuarios pueden ordenar una lista de palabras. El usuario puede elegir entre diferentes formas de ordenarlas:

- Orden alfabético ascendente

- Orden alfabético descendente

- Orden por longitud de palabra

Cada una de estas formas de ordenar es una estrategia diferente. Todas cumplen con una misma interfaz llamada, por ejemplo, IOrdenamiento, pero aplican un algoritmo distinto. El usuario puede cambiar la estrategia de ordenamiento en cualquier momento, sin afectar cómo funciona el resto de la aplicación.

Este es un caso ideal para aplicar el patrón Strategy ya que se definen varias estrategias que pueden cambiarse fácilmente sin modificar el código principal.

---

## Estructura del directorio
```
lab3/
└── strategy/
    ├── Program.cs
    ├── IOrdenamiento.cs
    ├── OrdenAlfabeticoAsc.cs
    ├── OrdenAlfabeticoDesc.cs
    ├── OrdenPorLongitud.cs
    └── Ordenador.cs
```
---

## ¿Cómo se prueba el patrón Strategy?

Una de las grandes ventajas del patrón Strategy es que facilita enormemente las pruebas unitarias, gracias a su enfoque en la **composición** y el **desacoplamiento**.


### Pruebas unitarias por estrategia

Cada estrategia implementa una interfaz común, por lo que se puede probar de forma aislada.

- Ejemplo usando **NUnit**:

```csharp
using NUnit.Framework;

[TestFixture]
public class OrdenAlfabeticoAscTests
{
    [Test]
    public void DeberiaOrdenarCorrectamente()
    {
        var estrategia = new OrdenAlfabeticoAsc();
        var entrada = new List<string> { "pera", "manzana", "kiwi" };
        var esperado = new List<string> { "kiwi", "manzana", "pera" };

        var resultado = estrategia.Ordenar(entrada);

        Assert.AreEqual(esperado, resultado);
    }
}
```

### Prueba del contexto con estrategia falsa (mock)

Podemos verificar que el contexto (Ordenador) delega correctamente la lógica a la estrategia usando una clase falsa o un framework de mocks (como Moq).

```csharp
using NUnit.Framework;
using Moq;

[TestFixture]
public class OrdenadorTests
{
    [Test]
    public void DeberiaLlamarAEstrategiaOrdenar()
    {
        var mockEstrategia = new Mock<IOrdenamiento>();
        var palabras = new List<string> { "uno", "dos" };

        mockEstrategia.Setup(e => e.Ordenar(It.IsAny<List<string>>()))
                      .Returns(palabras);

        var ordenador = new Ordenador();
        ordenador.EstablecerEstrategia(mockEstrategia.Object);

        ordenador.MostrarOrden(palabras);

        mockEstrategia.Verify(e => e.Ordenar(It.Is<List<string>>(l => l == palabras)), Times.Once);
    }
}
```

### Beneficios de testear con Strategy

- Las estrategias son independientes → pruebas más simples.

- El contexto puede ser probado con mocks o estrategias reales.

- Se asegura que el cliente usa pero no conoce la implementación de la estrategia (bajo acoplamiento).

---

## ¿Cómo ejecutar el ejemplo?

### Requisitos:
- Tener instalado [.NET SDK](https://dotnet.microsoft.com/download)

### Pasos:

1. Abrir una terminal en la carpeta donde está el proyecto (`strategy`)
2. Ejecutar el comando:
   ```bash
   dotnet run
   ```
3. Resultado esperado:

``` bash
Orden alfabético ascendente:
banana, kiwi, manzana, pera, uva

Orden alfabético descendente:
uva, pera, manzana, kiwi, banana

Orden por longitud:
uva, kiwi, pera, banana, manzana

```
---



