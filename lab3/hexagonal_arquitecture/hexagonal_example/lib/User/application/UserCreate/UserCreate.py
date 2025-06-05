from ...domain.UserRepository import UserRepository
from ...domain.User import User
from ...domain.UserId import UserId
from ...domain.UserEmail import UserEmail
from ...domain.UserName import UserName 

class UserCreate:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def run(self, id: str, name: str, email: str) -> User:
        """Create a new user and save it to the repository."""
        user = User(id=UserId(id), 
                    name=UserName(name), 
                    email=UserEmail(email))
        return self.user_repository.save(user)
        