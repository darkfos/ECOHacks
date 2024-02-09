# Aiogram
from aiogram import Router, types

#Локальные директивы

#Сторонние директивы


#Роутер для обычных сообщений
message_router: Router = Router()


@message_router.message()
async def get_all_messages(message: types.Message) -> None:
    await message.answer(text="Не понимаю о чём вы говорите!")