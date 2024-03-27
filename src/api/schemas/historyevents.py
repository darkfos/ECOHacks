import datetime

from pydantic import BaseModel, Field, validator


class AddHistoryEvent(BaseModel):

    message_history: str
    date_message: datetime.datetime = Field(default_factory=datetime.datetime.now)
    tg_id: int


class HistoryEvent(BaseModel):

    history_event_id: int
    message_history: str
    date_message: datetime.datetime = Field(default_factory=datetime.datetime.now)
    tg_id: int