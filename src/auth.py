from flask import session, abort
from src.models import User
from src import repository


def get_current_user() -> User | None:
    username = session.get("username")
    if not username:
        return None
    return repository.get_user(username)


def get_current_user_or_raise() -> User:
    user = get_current_user()
    if not user:
        abort(401)
    return user


def get_user_with_password_check(username: str, password: str) -> User | None:
    user = repository.get_user(username)
    if not user:
        return None
    if user.password != password:
        return None
    return user


def login(user: User):
    session["username"] = user.name


def logout():
    session.pop("username")
