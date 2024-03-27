import datetime

from pydantic import BaseModel, Field, field_validator


class AddReport(BaseModel):

    message_history: str = Field(max_length=200)
    tg_id: int
    photo: bytes
    latitude: float
    longtitude: float
    street_data: str
    date_report: datetime.datetime = Field(default_factory=datetime.datetime.now)


class Report(BaseModel):

    report_id: int
    message_history: str = Field(max_length=200)
    tg_id: int
    photo: bytes
    latitude: float
    longtitude: float
    street_data: str
    date_report: datetime.datetime = Field(default_factory=datetime.datetime.now)