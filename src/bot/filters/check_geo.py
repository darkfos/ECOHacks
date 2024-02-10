from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram import types


class GeoFilter(BaseFilter):
    async def __call__(self,
                       callback_message: types.Message, state: FSMContext) -> bool:
        if callback_message.text.lower() == "отправить гео-данные":
            return True
        return False