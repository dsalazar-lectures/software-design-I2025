class UserName:
    def __init__(self, name: str):
        self.name = name
        self.ensure_is_valid()

    def ensure_is_valid(self):
        if len(self.name) < 3:
            raise ValueError("User name must be at least 3 characters long")
