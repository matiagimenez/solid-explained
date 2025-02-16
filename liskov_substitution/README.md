# LSP: Liskov Substitution Principle

The Liskov Substitution Principle (LSP), the third of the five principles of SOLID, is a fundamental concept in object-oriented software development.

## Definition

This is a fundamental principle in object-oriented programming that states that **objects of a superclass should be able to be replaced with objects of a subclass** without affecting the correctness of the program.

This principle is named after Barbara Liskov, who first formulated it in a 1987 paper.

In simple words,

-   Objects of a superclass should be able to be replaced with objects of a subclass without affecting the program.
-   Object of subclass should be able to access the all the methods and properties of the superclass.

We will be violating Liskov's substitution principle when a subclass has unused methods of the parent class or methods that do not apply to the subclass we are creating.

Another case where the principle may be violated would be if a subclass redefines the method so that the return type of that method changes, for example if it must return a string and the subclass redefines it to a number we would be violating the principle since that subclass would not work in all contexts.

### Real world analogy

Imagine a delivery service company that has different types of vehicles: trucks, vans, and bikes. The company expects all vehicles to be able to complete deliveries, so they have a general process where a vehicle is assigned to deliver a package.

Now, a truck and a van can both be used for deliveries, but what happens if you try to send a bike on a long-haul delivery that requires a large capacity? The bike isn't designed for such a task and would fail to perform as expected. If a truck is replaced with a van or vice versa, everything works fine because they can handle the expected tasks similarly.

However, if you substitute the truck or van with a bike that isn’t capable of handling larger deliveries, it breaks the process because it can't fulfill the same role. This violates the Liskov Substitution Principle, which says that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

In software, this principle ensures that a subclass can be substituted for its parent class without introducing errors or unexpected behaviors, maintaining consistency and trust in the system.

## References

-   📚 [Liskov Substitution Principle (LSP)](https://tusharghosh09006.medium.com/liskov-substitution-principle-lsp-744eceb29e8)
-   📚 [Principios SOLID: (3) Liskov Substitution Principle](https://secture.com/principios-solid-3-liskov-substitution-principle/)
