import datetime
import json

from sqlalchemy import BigInteger, Integer, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    win_id: Mapped[int] = mapped_column(BigInteger, nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    last_send_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    sent_images: Mapped[list[str]] = mapped_column(Text, nullable=True, default=json.dumps([]))

class WinUser(Base):
    __tablename__ = "win_users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)