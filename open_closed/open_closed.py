"""
Open-Closed Principle (OCP) - "Extend, don’t modify."

A class should be open for extension but closed for modification.
"""

class Dish:
    def __init__(self, type: str) -> None:
        self.type: str = type
        
    def __str__(self) -> str:
        return (f"{self.get_description()} - ${self.get_price():.2f}")


    def get_description(self) -> str:
        """
        This method violates OCP because every time we add a new dish,
        we must modify this method.
        """
        if self.type == "pasta":
            return "Delicious Italian Pasta"
        elif self.type == "pizza":
            return "Cheesy Margherita Pizza"
        elif self.type == "burger":
            return "Juicy Beef Burger"
        else:
            return "Unknown Dish"

    def get_price(self) -> float:
        """
        This method also violates OCP for the same reason.
        Adding a new dish requires modifying existing code.
        """
        if self.type == "pasta":
            return 12.99
        elif self.type == "pizza":
            return 15.99
        elif self.type == "burger":
            return 10.99
        else:
            return 0.0
        
"""
❌ Problem:
- If we add a new dish (e.g., "Salad"), we must modify `get_description` and `get_price`,
  which breaks OCP.
- The class is not "closed for modification" because we keep changing its logic.
"""


from abc import ABC, abstractmethod

"""
Instead of modifying existing code to add new functionality, 
we extend the behavior using inheritance.
"""

class Dish(ABC):
    """
    The base `Dish` class defines an interface that all dishes must implement.
    This ensures that new dishes can be added without modifying existing code.
    """
    
    def __str__(self) -> str:
        return (f"{self.get_description()} - ${self.get_price():.2f}")

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

class Pasta(Dish):
    def get_description(self) -> str:
        return "Delicious Italian Pasta"

    def get_price(self) -> float:
        return 12.99

class Pizza(Dish):
    def get_description(self) -> str:
        return "Cheesy Margherita Pizza"

    def get_price(self) -> float:
        return 15.99

class Burger(Dish):
    def get_description(self) -> str:
        return "Juicy Beef Burger"

    def get_price(self) -> float:
        return 10.99


menu = [Pasta(), Pizza(), Burger()]
"""
✅ Solution:
- `Dish` class is "closed for modification" (existing code remains unchanged).
- New dishes can be added by creating subclasses (extending functionality).
- `print_menu` function works with any new dish without requiring changes.

To add a new dish like "Salad," we simply create:
"""

class Salad(Dish):
    def get_description(self) -> str:
        return "Fresh Garden Salad"

    def get_price(self) -> float:
        return 8.99

# Now, we can add Salad without modifying existing classes
menu.append(Salad())
