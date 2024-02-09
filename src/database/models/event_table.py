from database.db import PostBase
from sqlalchemy import BigInteger, Column, String, DATE, BLOB
from sqlalchemy.orm import Mapped, mapped_column


class EventTable(PostBase):
    """
    Таблица "События"
    """

    __tablename__ = "EventsTable"

    event_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: BigInteger = mapped_column(BigInteger)
    message: Mapped[str] = Column(String)
    data: DATE = Column(DATE)
    photo: BLOB = Column(BLOB)
