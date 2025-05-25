# Laboratory #3 Henry Rojas Fuentes
## Software Design Pattern: Decorator

### Definition:

The Decorator pattern is a structural pattern that allows adding additional functionalities to an object dynamically without modifying its original class. It is achieved by the following participants:

- ***Component***
Deﬁne the interface for objects that can have responsibilities added to them.
- ***Concrete Component***
Deﬁne an object to which additional responsibilities can be added.
- ***Decorator***
Maintains a reference to the associated component. Implements the interface of the Component superclass by delegating to the associated component.
- ***Decorator Concrete***
Adds responsibilities to the component.
### What is the common problem it solves?

- Add functionality to individual objects (not to an entire class) in a flexible way and without modifying the original source code, which can be crucial when working with already deployed or third-party code.

- Avoid proliferation of subclasses for each possible combination of functionality (which would occur with traditional inheritance).

### How does it improve the maintenance or scalability of the system?
- ***High cohesion and low coupling***: each decorator focuses on a single responsibility.
- ***Extensibility without modifying existing code (SOLID Open/Closed Principle)***: you can add new decorators for new functionalities without touching already developed classes.
- ***Behavior reuse***: you can reuse decorators in different contexts or combine them in different commands to obtain behavior variations.

### Advantages

- It allows extending behaviors at runtime.
- It is more flexible than inheritance.
- Complies with design principles such as Open/Closed and Single Responsibility.
- You can combine multiple decorators to build complex functionality in a modular way.

### Disadvantages

- ***Structural complexity***: can be difficult to follow if there are many nested decorators.
- ***Increased number of classes***: each functionality may require its own decorator, which can lead to an explosion of classes if not well managed.
- The order in which decorators are applied can affect behavior, which adds another point to consider.