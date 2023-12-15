from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]
    participants: Mapped[list["Participant"]] = relationship()
    mailbox_id: Mapped[int] = mapped_column(ForeignKey("mailbox.id"))
    mailbox: Mapped["Mailbox"] = relationship()


class Workspace(Base):
    __tablename__ = "workspace"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    participants: Mapped[list["Participant"]] = relationship()
    tasks: Mapped[list["Task"]] = relationship()


class Participant(Base):
    __tablename__ = "participant"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(ForeignKey("user.name"))
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))
    tasks: Mapped[list["Task"]] = relationship()
    role: Mapped[str] = mapped_column(default="teammate")


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    done: Mapped[bool] = mapped_column(default=False)
    assignee_id: Mapped[int] = mapped_column(ForeignKey("participant.id"))
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))


class Mailbox(Base):
    #  Обо всех приглашениях
    __tablename__ = "mailbox"

    id: Mapped[int] = mapped_column(primary_key=True)
    invitations: Mapped[list["Invitation"]] = relationship()
    user: Mapped["User"] = relationship()
    username: Mapped[str] = mapped_column(ForeignKey("user.name"))


class Invitation(Base):
    #  Одно приглашение
    __tablename__ = "invitation"

    id: Mapped[int] = mapped_column(primary_key=True)
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))
    workspace: Mapped["Workspace"] = relationship()
    mailbox_id: Mapped[int] = mapped_column(ForeignKey("mailbox.id"))
