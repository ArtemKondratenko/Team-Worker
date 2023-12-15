from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "user"
    name: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]
