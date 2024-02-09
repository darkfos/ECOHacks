from database.db import PostBase
from sqlalchemy import BigInteger, Column, String, DATE, BLOB
from sqlalchemy.orm import Mapped, mapped_column


class UserTable(PostBase):
    """
    Таблица "User"
    """
    __tablename__ = "UserTable"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_user: String = Column(String)
    tg_id: BigInteger = mapped_column(BigInteger)
    date_registration: DATE = Column(DATE)