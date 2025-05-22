# Laboratory #3

## Design Pattern: Adapter  
**Student Name:** Jorge Quiros Anderson 
**Selected Topic:** Adapter

---

### What is the Adapter Pattern?

The Adapter pattern is a structural design pattern that allows incompatible interfaces to work together. It acts as a "bridge" between two classes, adapting the interface of one class to what the client expects.

---

### What Problem Does It Solve?

It enables systems that use different interfaces to collaborate without needing to change their original code. This pattern is useful when integrating new components into an existing system whose design cannot (or should not) be modified.

**Problem Example:**  
Suppose you have a class that expects data from an API in a specific format, but the new API you need to use returns data in a different format. The Adapter pattern can transform this data at runtime without modifying the original logic of the consuming class.

---

### How Does It Improve Maintainability or Scalability?

- **Maintainability:**  
  It keeps responsibilities separated and prevents high-level classes from depending on low-level implementation details.

- **Scalability:**  
  It simplifies the integration of new data sources, services, or APIs without altering the rest of the system—new adapters can simply be added.

---

### Advantages

- Isolates client code from changes in adapted classes.  
- Encourages the **Single Responsibility Principle**.  
- Supports the **Open/Closed Principle** (new adapters can be added without modifying existing code).  

---

### Disadvantages

- May increase system complexity if overused.  
- Can hide deeper design issues if used as a shortcut to avoid proper refactoring.


---

## Adapter Pattern Example (Java)

This project demonstrates the **Adapter Design Pattern** in Java.

### Structure

- `RoundPeg` and `RoundHole` are naturally compatible.
- `SquarePeg` is not compatible with `RoundHole`.
- `SquarePegAdapter` allows `SquarePeg` to be used where `RoundPeg` is expected.

### Project Structure

```
adapter/
└── adapter/
├── Demo.java
├── round/
│ ├── RoundHole.java
│ └── RoundPeg.java
├── square/
│ └── SquarePeg.java
└── adapters/
└── SquarePegAdapter.java
```

### Compilation

```bash
javac -d out lab3/adapter/**/*.java
```

### Execution
```bash
java -cp out adapter.Demo
```
### Output

```bash
Round peg r5 fits round hole r5.
Square peg w2 fits round hole r5.
Square peg w20 does not fit round hole r5.
```
### Reference

This implementation is inspired by the official Adapter pattern example from Refactoring Guru:
https://refactoring.guru/es/design-patterns/adapter/java/example

---
## Ejemplo de un adapter en una situacion real:
En un sistema web, por ejemplo una aplicación en React o Angular que consume múltiples APIs, cada una puede tener diferentes estructuras JSON. Si el frontend espera una estructura específica pero cada proveedor envía datos distintos, podríamos crear Adapters de datos en el backend (Node.js, Java, etc.) o incluso en el frontend para transformar los datos a un formato común antes de pasarlos a los componentes.
Ejemplo concreto:

- **API A devuelve:**
```bash
{ 
  fullName: "Jorge Quiros", "email": "jorge@example.com" 
}
```

- **API B devuelve:**
```bash
{ 
  name: "Jorge", "surname": "Quiros", "contact": { "mail": "jorge@example.com" } 
}
```

- **Estructura esperada por la aplicación:**
```bash
{
  fullName: "Jorge Quiros",
  email: "jorge@example.com"
}
```

- **Implemetación del adapter:**
```bash
function adaptUserFromApiB(data) {
  return 
  {
    fullName: `${data.name} ${data.surname}`,
    email: data.contact.mail,
  };
}
```
