from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class User(BaseModel):
    user_id: int
    name_user: str = Field(max_length=350)
    tg_id: int
    date_reg: datetime = Field(default_factory=datetime.now)


class UserAdd(BaseModel):
    name_user: str = Field(max_length=350)
    tg_id: int
    date_reg: datetime = Field(default_factory=datetime.now)