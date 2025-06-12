from abc import ABC, abstractmethod

from .User import User
from .UserId import UserId

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        """Save a user to the repository."""
        pass

    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User | None:
        """Find a user by their ID."""
        pass

    @abstractmethod
    def find_all(self) -> list[User]:
        """Find all users in the repository."""
        pass

    @abstractmethod
    def delete(self, user_id: UserId) -> None:
        """Delete a user by their ID."""
        pass