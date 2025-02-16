# DIP: Dependency Inversion Principle

The Dependency Inversion Principle (SRP), the fifth of the five principles of SOLID, is a fundamental concept in object-oriented software development.

## Definition

This principle emphasizes decoupling and abstraction. The principle consists of two core concepts: **high-level modules should not depend on low-level modules**, and **both should depend on abstractions**. This inverted dependency relationship promotes flexibility, testability, and maintainability.

By introducing abstractions, high-level modules are no longer directly dependent on low-level modules. This loose coupling allows for independent development, modification, and replacement of individual components.

Abstractions make it easier to write unit tests by enabling the use of mock objects or test doubles. With dependencies abstracted away, I can isolate and test individual modules more effectively.

### Real world analogy

Imagine a car manufacturing company. The company designs cars, but instead of building every single part of the car in-house, they rely on specialized suppliers to provide the parts: engines, tires, seats, etc. The car manufacturer doesn't directly depend on a specific engine type or tire type; instead, they depend on a general contract with the suppliers that specifies the type of part required.

This allows the car company to easily swap out suppliers or change parts without redesigning the whole car. If one engine supplier fails, they can easily find another that meets the same specifications.

Similarly, in software, classes or components should depend on abstractions rather than on concrete implementations. By depending on abstractions, we can easily replace or modify parts of the system without affecting the entire application, which results in a more flexible and maintainable design.

## References

-   📚 [SOLID — Dependency Inversion Principle](https://medium.com/@inzuael/solid-dependency-inversion-principle-part-5-f5bec43ab22e)
