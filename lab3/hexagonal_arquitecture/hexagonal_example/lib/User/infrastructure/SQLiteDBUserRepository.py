from ..domain.UserRepository import UserRepository
from ..domain.User import User
from ..domain.UserId import UserId
from ..domain.UserEmail import UserEmail
from ..domain.UserName import UserName
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def to_domain(self) -> User:
        return User(id=UserId(self.id), name=UserName(self.name), email=UserEmail(self.email))

class SQLiteDBUserRepository(UserRepository):
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, user: User) -> None:
        session = self.Session()
        try:
            # Check if the user already exists
            existing_user = session.query(UserModel).filter_by(id=user.id.user_id).first()
            if existing_user:
                # Update existing user
                existing_user.name = user.name.name
                existing_user.email = user.email.email
            else:
                # Create a new user
                user_model = UserModel(id=user.id.user_id, name=user.name.name, email=user.email.email)
                session.add(user_model)
            session.commit()
            return user
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def find_by_id(self, id: UserId) -> User | None:
        """Find a user by their ID in the MariaDB database."""
        session = self.Session()
        try:
            user_model = session.query(UserModel).filter_by(id=id.user_id).first()
            return user_model.to_domain() if user_model else None
        except SQLAlchemyError as e:
            raise e
        finally:
            session.close()

    def find_all(self) -> list[User]:
        """Find all users in the MariaDB database."""
        session = self.Session()
        try:
            user_models = session.query(UserModel).all()
            return [user_model.to_domain() for user_model in user_models]
        except SQLAlchemyError as e:
            raise e
        finally:
            session.close()
    
    def delete(self, id: UserId) -> None:
        """Delete a user by their ID from the MariaDB database."""
        session = self.Session()
        try:
            user_model = session.query(UserModel).filter_by(id=id.user_id).first()
            if user_model:
                session.delete(user_model)
                session.commit()
            else:
                raise KeyError(f"User with ID {id.user_id} not found.")
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()