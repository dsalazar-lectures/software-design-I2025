class UserNotFoundError(Exception):
    """Exception raised when a user is not found in the system."""
    
    def __init__(self, user_id: str):
        super().__init__(f"User with ID '{user_id}' not found.")
        self.user_id = user_id

    def __str__(self):
        return f"UserNotFoundError: {self.user_id}"