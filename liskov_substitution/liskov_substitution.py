"""
Liskov Substitution Principle (LSP) - “I know I can trust you to do what I expect you to do!”

A subclass should extend a superclass without changing its behavior.
"""

"""
❌ Violations:
- `Penguin` is a `Bird`, but it cannot fly.
- Code expecting a `Bird` should work with any subclass.
- `make_bird_fly(penguin)` breaks because `Penguin.fly()` raises an error.
"""
class Bird:
    def fly(self) -> str:
        return "I can fly!"

class Sparrow(Bird):
    pass  # ✅ Inherits `fly` behavior correctly

class Penguin(Bird):
    """
    ❌ Problem: Penguins cannot fly, but they inherit `fly` from Bird.
    If a function expects a `Bird` and calls `fly()`, it will break when given a Penguin.
    """
    def fly(self) -> str:
        raise NotImplementedError("Penguins cannot fly!")

# Function that expects a Bird
def make_bird_fly(bird: Bird) -> None:
    print(bird.fly())

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # ✅ Works fine
make_bird_fly(penguin)  # ❌ Runtime error! Violates LSP.

"""
✅ Solution: Separate the ability to fly into an interface.
Birds that can fly will implement `FlyingBird`, while non-flying birds will not.

- `Penguin` is no longer forced to implement `fly()`, avoiding errors.
- `make_bird_sound()` works for all birds.
- `make_bird_fly()` only works for birds that can fly.
- No unexpected behavior, fully follows LSP.
"""
from abc import ABC, abstractmethod

class Bird(ABC):
    """
    The base `Bird` class ensures all birds have a `sound()` method
    but does not assume all can fly.
    """

    @abstractmethod
    def sound(self) -> str:
        pass

class FlyingBird(Bird, ABC):
    """
    `FlyingBird` extends `Bird` and adds a `fly()` method.
    Only birds that can fly will inherit from this class.
    """

    @abstractmethod
    def fly(self) -> str:
        pass

class Sparrow(FlyingBird):
    def sound(self) -> str:
        return "Chirp Chirp"

    def fly(self) -> str:
        return "I can fly!"

class Penguin(Bird):
    def sound(self) -> str:
        return "Honk Honk"  # Penguins make sound but cannot fly

# Function that works with any bird
def make_bird_sound(bird: Bird) -> None:
    print(bird.sound())

# Function that works only with flying birds
def make_bird_fly(bird: FlyingBird) -> None:
    print(bird.fly())

sparrow = Sparrow()
penguin = Penguin()

make_bird_sound(sparrow)  # ✅ Works
make_bird_sound(penguin)  # ✅ Works

make_bird_fly(sparrow)  # ✅ Works
# make_bird_fly(penguin)  # ❌ Type error: Penguin is not a FlyingBird