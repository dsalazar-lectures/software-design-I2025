from ...Shared.infrastructure.ServiceContainer import ServiceContainer
from ...User.domain.UserNotFoundError import UserNotFoundError

class ConsoleInterface:
    def __init__(self):
        self.service_container = ServiceContainer()

    def run(self) -> None:
        """Run the console interface for user management."""
        while True:
            print("1. Get all users")
            print("2. Create user")
            print("3. Get user by ID")
            print("4. Delete user")
            print("5. Edit user")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.get_all_users()
            elif choice == "2":
                self.create_user()
            elif choice == "3":
                self.get_user_by_id()
            elif choice == "4":
                self.delete_user()
            elif choice == "5":
                self.edit_user()
            elif choice == "6":
                break
            else:
                print("Invalid option, please try again.")

    def get_all_users(self):
        users = self.service_container.user_get_all().run()
        for user in users:
            print(f"ID: {user.id.user_id}, Name: {user.name.name}, Email: {user.email.email}")

    def create_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        try:           
          self.service_container.user_create().run(user_id, name, email)
        except Exception as e:
            print(f"An error occurred while creating the user: {e}")
            return
        print("User created successfully.")

    def get_user_by_id(self):
        user_id = input("Enter user ID: ")
        try:
            user = self.service_container.get_user_by_id().run(user_id)
            print(f"ID: {user.id.user_id}, Name: {user.name.name}, Email: {user.email.email}")
        except UserNotFoundError:
            print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_user(self):
        user_id = input("Enter user ID to delete: ")
        try:
            self.service_container.user_delete().run(user_id)
            print("User deleted successfully.")
        except UserNotFoundError:
            print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def edit_user(self):
        user_id = input("Enter user ID to edit: ")
        name = input("Enter new user name: ")
        email = input("Enter new user email: ")
        try:
            self.service_container.user_edit().run(user_id, name, email)
            print("User edited successfully.")
        except UserNotFoundError:
            print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")