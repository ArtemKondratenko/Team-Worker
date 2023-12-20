from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedAsDataclass
from sqlalchemy import ForeignKey
from src.database import db


class User(db.Model, MappedAsDataclass):
    name: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]
    participants: Mapped[list["Participant"]] = relationship(init=False)
    mailbox: Mapped["Mailbox"] = relationship(back_populates="user", init=False)


class Workspace(db.Model, MappedAsDataclass):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    description: Mapped[str]
    participants: Mapped[list["Participant"]] = relationship(init=False)
    tasks: Mapped[list["Task"]] = relationship(init=False)


class Participant(db.Model, MappedAsDataclass):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str] = mapped_column(ForeignKey("user.name"))
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))
    tasks: Mapped[list["Task"]] = relationship(init=False)
    role: Mapped[str] = mapped_column(default="teammate")


class Task(db.Model, MappedAsDataclass):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    description: Mapped[str]
    assignee_id: Mapped[int] = mapped_column(ForeignKey("participant.id"))
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))
    done: Mapped[bool] = mapped_column(default=False)


class Mailbox(db.Model, MappedAsDataclass):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    invitations: Mapped[list["Invitation"]] = relationship(init=False)
    user: Mapped["User"] = relationship(back_populates="mailbox", init=False)
    username: Mapped[str] = mapped_column(ForeignKey("user.name"))


class Invitation(db.Model, MappedAsDataclass):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))
    workspace: Mapped["Workspace"] = relationship(init=False)
    mailbox_id: Mapped[int] = mapped_column(ForeignKey("mailbox.id"))
