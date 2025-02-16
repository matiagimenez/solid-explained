# ISP: Interface Segregation Principle

The Interface Segregation Principle (ISP), the fourth of the five principles of SOLID, is a fundamental concept in object-oriented software development.

## Definition

This principle suggests that **a class should not be forced to implement methods it doesn’t need**. In other words, a class should have small, focused interfaces rather than large, monolithic ones. This helps to avoid unnecessary dependencies and ensures that classes only implement the methods they actually need.

Smaller, more focused interfaces are easier to understand and implement and also simplifies the maintenance of the system by reducing the likelihood of unintended side effects when interfaces change.

### Real world analogy

Imagine a gym where there are different types of personal trainers. Some trainers specialize in weightlifting, others in yoga, and some in cardio training. If every trainer was required to know and teach all of these activities, it would result in inefficiency. A yoga trainer, for instance, shouldn't be forced to learn or teach weightlifting, as it's not part of their expertise.

In a well-organized gym, each trainer specializes in what they do best, and they only interact with clients who need their specific services.

Similarly, in software, classes or interfaces should focus on the specific tasks or responsibilities they are intended to handle. Forcing a class to implement unnecessary methods that it doesn’t need or understand is inefficient and can lead to a bloated system. Instead, interfaces should be broken into smaller, more specialized ones to allow for cleaner, more focused designs.

## References

-   📚 [SOLID: I - Interface Segregation Principle (ISP)](https://dev.to/paulocappa/solid-i-interface-segregation-principle-isp-385f)
-   📚 [Interface Segregation Principle (ISP): SOLID Principle](https://medium.com/@ramdhas/4-interface-segregation-principle-isp-solid-principle-39e477bae2e3)
