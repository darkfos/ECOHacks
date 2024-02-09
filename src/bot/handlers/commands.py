# Aiogram

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile

# Локальные директивы
from src.bot import text

# Сторонние библиотеки
import logging

commands_router: Router = Router()


@commands_router.message(CommandStart())
async def com_start(message: types.Message):
    """
    Асинхронная функция для команды старт, отправляем фото, начальную инфу.
    :param message:
    :return:
    """

    # Фото
    path = r"static\for_start.png"
    photo_to_send: FSInputFile = FSInputFile(path)
    logging.info(msg="Пользователь {} отправил запрос на команду /start".format(message.from_user.full_name))
    await message.answer_photo(photo=photo_to_send, caption=await text.get_message_start(message.from_user.full_name), parse_mode="HTML")


@commands_router.message(Command("help"))
async def com_help(message: types.Message):
    logging.info(msg="Пользователь {} отправил запрос на команду /help".format(message.from_user.full_name))
    await message.answer(text=await text.get_message_help(), parse_mode="HTML")