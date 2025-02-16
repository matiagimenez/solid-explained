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

Imagine you are at a library, and the library has a collection of books organized into categories, such as Fiction, Non-fiction, and Science.

The book concept represents the general idea of any book in the library.
Specific categories like fiction books, non-fiction books, and science books represent more specialized types of books.

## References

-   📚 [Liskov Substitution Principle (LSP)](https://tusharghosh09006.medium.com/liskov-substitution-principle-lsp-744eceb29e8)
-   📚 [Principios SOLID: (3) Liskov Substitution Principle](https://secture.com/principios-solid-3-liskov-substitution-principle/)
