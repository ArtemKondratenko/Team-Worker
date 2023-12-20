from src.database import db
from src.models import User, Workspace, Participant


def add_user(name: str, password: str):
    """Add user in the database"""
    user = get_user(name)
    if user:
        raise ValueError(f"Пользователь {name} уже существует!")
    user = User(name=name, password=password)
    db.session.add(user)
    db.session.commit()


def get_user(name: str) -> User | None:
    user = db.session.get(User, name)
    return user


def save_workspace_in_db(workspace: Workspace):
    db.session.add(workspace)
    db.session.commit()


def save_participant_in_db(participant: Participant):
    db.session.add(participant)
    db.session.commit()


def get_workspace(workspace_id: int) -> Workspace | None:
    workspace = db.session.get(Workspace, workspace_id)
    return workspace
