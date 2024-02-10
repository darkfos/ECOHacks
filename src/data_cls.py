import datetime
from dataclasses import dataclass

"""
    Дата классы для удобного хранения информации. А так же более удобной сортировки, обработки
"""


@dataclass
class UserInfo:
    name_user: str
    tg_id: int
    date_reg: datetime.datetime


@dataclass
class EventInfo:
    tg_id: int
    message_event: str
    date_event: datetime.datetime
    photo: bytes


@dataclass
class HistoryEventInfo:
    message_history: str
    date_message: datetime.datetime
    tg_id: int