# Aiogram

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext

# Локальные директивы
from src.bot import text
from src.bot import ReportUser

# Сторонние библиотеки
import logging

commands_router: Router = Router()


@commands_router.message(CommandStart())
async def com_start(message: types.Message) -> None:
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
async def com_help(message: types.Message) -> None:
    """
    Асинхронная функция для команды 'help', отправляет текстовый список имеющихся команд
    :param message:
    :return:
    """

    logging.info(msg="Пользователь {} отправил запрос на команду /help".format(message.from_user.full_name))
    await message.answer(text=await text.get_message_help(), parse_mode="HTML")


@commands_router.message(Command("report"))
async def com_report(message: types.Message, state: FSMContext) -> None:
    """
    Асинхронная функция для команды 'report', загружает состояние -> ReportUser
    :param message:
    :param state:
    :return:
    """

    logging.info(msg="Пользователь {} отправил запрос на команду /report".format(message.from_user.full_name))
    await message.answer(text="Хорошо, что вы нашли непрестойное место! Жду ваше текстовое пояснение об объекте!")
    await state.set_state(ReportUser.message_text)


@commands_router.message(Command("clear"))
async def com_clear(message: types.Message, state: FSMContext) -> None:
    """
    Асинхронная функция для команды 'clear', очищаем на данный момент состояние
    :param message:
    :param state:
    :return:
    """

    #Очистка состояния
    await state.clear()
    await message.answer(text="Очистка была успешно проведена!")

