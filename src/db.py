from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import Base
from src.models.user import User

engine = create_engine("sqlite:///testdb")
Session = sessionmaker(bind=engine)


def create_db():
    Base.metadata.create_all(engine)


def add_user(name: str, password: str):
    """Add user in the database"""
    with Session() as session:
        user = get_user(name)
        if user:
            raise ValueError(f"Пользователь {name} уже существует!")
        user = User(name=name, password=password)
        session.add(user)
        session.commit()


def get_user(name: str) -> User | None:
    with Session() as session:
        user = session.get(User, name)
        return user
