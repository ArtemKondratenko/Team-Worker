from flask import session
from src.models.user import User
from src import db


def get_current_user() -> User | None:
    if username := session.get("username"):
        return db.get_user(username)


def get_user_with_password_check(username: str, password: str) -> User | None:
    user = db.get_user(username)
    if not user:
        return None
    if user.password != password:
        return None
    return user


def login(user: User):
    session["username"] = user.name


def logout():
    session.pop("username")
