import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    name_user: str
    tg_id: int
    date_reg: datetime.datetime


class UserSchemaUpdate(BaseModel):
    id_user: int
    name_user: str