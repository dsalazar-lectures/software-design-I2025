from ..domain.UserRepository import UserRepository
from ..domain.User import User
from ..domain.UserId import UserId

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def save(self, user: User) -> User:
        """ Save a user to the in-memory repository. """
        self.users[user.id.user_id] = user
        return user
    
    def find_by_id(self, id: UserId) -> User | None:
        """ Find a user by their ID in the in-memory repository. """
        return self.users.get(id.user_id, None)
    
    def find_all(self) -> list[User]:
        """ Find all users in the in-memory repository. """
        return list(self.users.values())
    
    def delete(self, id: UserId) -> None:
        """ Delete a user by their ID from the in-memory repository. """
        if id.user_id in self.users:
            del self.users[id.user_id]
        else:
            raise KeyError(f"User with ID {id.user_id} not found.")
    