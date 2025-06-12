from .UserId import UserId
from .UserName import UserName
from .UserEmail import UserEmail

class User:
    """User entity representing a user in the system."""
    def __init__(self, id: UserId, name: UserName, email: UserEmail):
        self.id = id
        self.name = name
        self.email = email
        
    def get_name_and_email(self) -> str:
        """Return the user's name and email as a formatted string."""
        return f"{self.name.name} <{self.email.email}>"