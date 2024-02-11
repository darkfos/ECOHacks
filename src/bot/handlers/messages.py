# Aiogram
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram import F

#Локальные директивы
...

#Сторонние директивы
import logging

#Роутер для обычных сообщений
message_router: Router = Router()

@message_router.message()
async def get_all_messages(message: types.Message) -> None:
    """
    Асинхронный модуль для обработки остального текста
    """

    await message.answer(text="Не понимаю о чём вы говорите!")