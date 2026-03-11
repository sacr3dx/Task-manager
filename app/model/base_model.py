from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional, List


class Base(DeclarativeBase):
    pass


class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[Optional[str]]
    deadline: Mapped[Optional[int]]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["ProfileModel"] = relationship(back_populates="tasks")

class ProfileModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str]
    tasks: Mapped[List["TaskModel"]] = relationship(back_populates="user")