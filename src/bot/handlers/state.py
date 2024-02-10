# Aiogram
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

#Локальные директивы
from src.bot.states import ReportUser

#Сторонние директивы
state_router: Router = Router()


@state_router.message(ReportUser.message_text)
async def message_from_user(message: types.Message, state: FSMContext) -> None:
    """
    Обработка состояния, сообщения от пользователя
    :param message:
    :param state:
    :return:
    """
    await state.update_data(message_text=message.text)
    await state.set_state(ReportUser.tg_id)
    await state.update_data(tg_id=message.from_user.id)
    await message.answer(text="Замечательно, жду фото")
    await state.set_state(ReportUser.photo_user)


@state_router.message(ReportUser.photo_user)
async def photo_from_user(message: types.Message, state: FSMContext) -> None:
    """
    Обработка состояния, фото от пользователя
    :param message:
    :param state:
    :return:
    """
    if message.from_user is message.photo:
        await state.update_data(photo_user=message.photo)
        await message.answer(text="Отлично. Жду гео данные!")
        await state.set_state(ReportUser.geo_position)
    else:
        await message.answer(text="Извините, но вы отправили совсем не фото! Жду повторную отправку.")


@state_router.message(ReportUser.geo_position)
async def geo_position(message: types.Message, state: FSMContext) -> None:
    """
    Обработка состояния, гео данные от пользователя
    :param message:
    :param state:
    :return:
    """
    await state.update_data(geo_position=message.text)

    all_data: dict = await state.get_data()

    #Очистка состояния
    await state.clear()