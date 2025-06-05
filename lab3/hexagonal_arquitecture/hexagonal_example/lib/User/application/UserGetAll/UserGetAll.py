from ...domain.UserRepository import UserRepository
from ...domain.User import User

class UserGetAll:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def run(self) -> list[User]:
        """Retrieve all users from the repository."""
        return self.user_repository.find_all()