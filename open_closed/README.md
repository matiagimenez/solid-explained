# OCP: Open-Closed Principle

The Open-Closed Principle (OCP), the second of the five principles of SOLID, is a fundamental concept in object-oriented software development.

## Definition

The principle states that objects or entities should be **open for extension but closed for modification**. This means they should be extendable without altering their core implementation.

This principle can be applied in Object-Oriented Programming (OOP) by creating new classes that extend the original class and override its methods, rather than modifying the original class directly.

In functional programming, this can be achieved through the use of function wrappers, where you can call the original function and apply new functionality to it without changing the original function itself.

Open/closed principle is intended to mitigate risk when introducing new functionality. Since you don't modify existing code you can be assured that it wouldn't be broken. It reduces maintenance cost and increases product stability.

### Real world analogy

A restaurant menu is can serve as an analogy for this principle.

The menu is open for extension because the restaurant can add new dishes or special items without removing the existing ones.

It is closed for modification because the existing dishes and their recipes don’t need to be altered every time a new dish is introduced.

In software, a well-designed system allows for new features (new menu items) to be added without modifying the core functionality (existing recipes).

## References

-   📚 [Open-Closed Principle: Extending Your Code Without Modification](https://medium.com/@reer217/open-closed-principle-extending-your-code-without-modification-523109ccfec2)

-   📚 [What is the meaning and reasoning behind the Open/Closed Principle?](https://stackoverflow.com/questions/59016/what-is-the-meaning-and-reasoning-behind-the-open-closed-principle)
