from ...domain.UserRepository import UserRepository
from ...domain.User import User
from ...domain.UserId import UserId
from ...domain.UserNotFoundError import UserNotFoundError

class GetUserGetUserById:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def run(self, id: str) -> User:
        """Retrieve a user by their ID from the repository."""
        user_id = UserId(id)
        user = self.user_repository.find_by_id(user_id)
        # If the user is not found, raise a UserNotFoundError
        if user is None:
            raise UserNotFoundError(user_id)
        return user