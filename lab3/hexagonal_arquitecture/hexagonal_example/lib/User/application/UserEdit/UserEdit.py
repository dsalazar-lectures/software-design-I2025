from ...domain.UserRepository import UserRepository
from ...domain.User import User
from ...domain.UserId import UserId
from ...domain.UserName import UserName
from ...domain.UserEmail import UserEmail
from ...domain.UserNotFoundError import UserNotFoundError

class UserEdit:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def run(self, id: str, name: str, email: str) -> User:
        """Edit an existing user and save the changes to the repository."""
        user_id = UserId(id)
        user = self.user_repository.find_by_id(user_id)
        
        # If the user is not found, raise a UserNotFoundError
        if user is None:
            raise UserNotFoundError(id)
        
        # Update the user's details
        user.name = UserName(name)
        user.email = UserEmail(email)
        
        # Save the updated user back to the repository
        return self.user_repository.save(user)