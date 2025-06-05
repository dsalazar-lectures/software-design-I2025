class UserEmail:
    def __init__(self, email: str):
        self.email = email
        self.is_valid_email()

    def is_valid_email(self):
        if '@' not in self.email or '.' not in self.email.split('@')[-1]:
            raise ValueError("Invalid email format")
