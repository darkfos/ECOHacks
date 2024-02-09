from aiogram.fsm.state import StatesGroup, State


class ReportUser(StatesGroup):
    """
    Состояние - Репорта
    """

    message_text: str = State()
    tg_id: int = State()
    photo_user: bytes = State()
    geo_position: str = State()
