from database.db import PostBase
from sqlalchemy import BigInteger, Column, String, DATE, BLOB, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class HistoryEventTable(PostBase):
    """
    Таблица "History"
    """

    __tablename__ = "HistoryEventTable"

    history_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str] = Column(String)
    date_message: DATE = Column(DATE)
    user_id: Mapped[int] = mapped_column(ForeignKey("EventsTable.event_id"))