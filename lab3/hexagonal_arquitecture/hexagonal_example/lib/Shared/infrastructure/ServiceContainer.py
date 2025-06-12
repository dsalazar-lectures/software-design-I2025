from ...User.infrastructure.InMemoryUserRepository import InMemoryUserRepository
from ...User.infrastructure.SQLiteDBUserRepository import SQLiteDBUserRepository



from ...User.application.UserGetAll.UserGetAll import UserGetAll
from ...User.application.UserCreate.UserCreate import UserCreate
from ...User.application.GetUserById.GetUserById import GetUserGetUserById
from ...User.application.UserDelete.UserDelete import UserDelete
from ...User.application.UserEdit.UserEdit import UserEdit

sqlyte = SQLiteDBUserRepository("sqlite:///mi_base.db")
memory = InMemoryUserRepository()

class ServiceContainer:
    def __init__(self):
        # Unique repository instance for the application
        self.user_repository = sqlyte

    def user_get_all(self) -> UserGetAll:
        """Returns an instance of UserGetAll."""
        return UserGetAll(self.user_repository)
    def user_create(self) -> UserCreate:
        """Returns an instance of UserCreate."""
        return UserCreate(self.user_repository)
    def get_user_by_id(self) -> GetUserGetUserById:
        """Returns an instance of GetUserGetUserById."""
        return GetUserGetUserById(self.user_repository)
    def user_delete(self) -> UserDelete:
        """Returns an instance of UserDelete."""
        return UserDelete(self.user_repository)
    def user_edit(self) -> UserEdit:
        """Returns an instance of UserEdit."""
        return UserEdit(self.user_repository)