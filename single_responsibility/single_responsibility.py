"""
Single Responsibility Principle (SRP) - “…You had one job” 

A class should have only one reason to change, meaning it should only have one responsibility.
"""

class User:
    def __init__(self, username: str):
        self.username = username
    
    def get_username(self) -> str:
        return self.username

    def save_to_database(self) -> User:
        # Code to save the user to a database
        pass

"""
The `User` class violates SRP because it has two responsibilities:
1. Managing user properties (`username`, `get_username`).
2. Handling database storage (`save_to_database`).

This design creates coupling between business logic (user properties) and persistence logic (database operations). If database management changes, we need to modify the `User` class, which should ideally remain focused only on user properties.
"""

class User:
    def __init__(self, username: str):
        self.username = username
    
    def get_username(self) -> str:
        return self.username

class UserRepository:
    def save(self, user: User) -> User:
        # Code to save the user to a database
        pass
    
    def get(self, id: int) -> User:
        # Code to fetch the user from a database
        pass

"""
Now, `User` only manages user properties, while `UserRepository` is responsible for persistence.

One downside of strict separation is that clients of this code now need to handle two classes. 

To simplify, we can use a Facade pattern. With this approach, `UserService` acts as a Facade, combining both concerns without violating SRP. 
Clients can interact with a single class while maintaining separation of concerns internally.
"""

class UserService:
    def __init__(self, username: str):
        self.user = User(username)
        self.db = UserRepository()

    def get_username(self) -> str:
        return self.user.get_username()
    
    def save(self) -> User:
        self.db.save(self.user)