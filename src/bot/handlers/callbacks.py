# Aiogram
import logging

from aiogram import Router, types
from aiogram.fsm.context import FSMContext

callback_router: Router = Router()

# Локальные директивы
from src.bot.filters import GeoFilter
from src.bot.states import ReportUser

# Сторонние директивы
...

@callback_router.callback_query(GeoFilter())
async def get_geo_data(message: types.Message, state: FSMContext):
    """
    Асинхронный модуль для получения гео данных
    """

    logging.info(msg="Пользователь {0} отправил свои гео данные".format(message.from_user.id))
    print(message.location)
    print(message.location.latitude)
    #await state.update_data(latitude=callbackMess.location.latitude)
    #await state.update_data(longitude=callbackMess.location.longitude)
    #print(await state.get_data())
    #await state.set_state(ReportUser.street_data)
    #await callbackMess.answer(text="Отлично, ваши данные были сохранены, спасибо!")
