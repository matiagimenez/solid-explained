# SRP: Single Responsibility Principle

The Single Responsibility Principle (SRP), the first of the five principles of SOLID, is a fundamental concept in object-oriented software development.

## Definition

This principle states that a class should have **only one reason to change**, meaning it should be responsible for only one part of the software’s functionality.

If a class has multiple responsibilities, it becomes tightly coupled. A change in one responsibility will likely require changes in another, making the code harder to maintain and modify.

Classes focused on a single responsibility are easier to test because you do not have to deal with multiple functionalities during the testing of a specific functionality.

### Real world analogy

Imagine a team in a restaurant. In this team, we have various functions: cooks, waiters, and the manager. Each of these team members has a unique responsibility. The cooks prepare the food, the waiters serve the food to the customers, and the manager takes care of the restaurant’s administration. Imagine the chaos if a single person tried to perform all these tasks, it would generate a totally inefficient and confusing system.

Similarly, a class in software should specialize in a single functionality or responsibility.

## References

-   📚 [The Single Responsibility Principle (SRP) of SOLID](https://giovannamoeller.medium.com/the-single-responsibility-principle-srp-of-solid-eb2feed0c64b)

-   📚 [SOLID: The First 5 Principles of Object Oriented Design](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
