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
make
```

### Execution
```bash
make run
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
## Example of an Adapter in a Real-World Scenario:
In a web system—such as a React or Angular application that consumes multiple APIs—each API may return data in different JSON structures. If the frontend expects a specific structure but each provider sends data differently, we can create data adapters either in the backend (Node.js, Java, etc.) or even on the frontend to transform the data into a common format before passing it to the components.

Concrete example:
- **API A returns:**
```bash
{ 
  fullName: "Jorge Quiros", "email": "jorge@example.com" 
}
```

- **API B returns:**
```bash
{ 
  name: "Jorge", "surname": "Quiros", "contact": { "mail": "jorge@example.com" } 
}
```

- **Expected structure by the application:**
```bash
{
  fullName: "Jorge Quiros",
  email: "jorge@example.com"
}
```

- **Adapter implementation:**
```bash
function adaptUserFromApiB(data) {
  return 
  {
    fullName: `${data.name} ${data.surname}`,
    email: data.contact.mail,
  };
}
```
