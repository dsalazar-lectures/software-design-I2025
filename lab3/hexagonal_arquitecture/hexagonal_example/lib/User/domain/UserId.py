class UserId:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.ensure_is_valid()

    def ensure_is_valid(self):
        if len(self.user_id) < 5:
            raise ValueError("User ID must be at least 5 characters long")
        