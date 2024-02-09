# Aiogram
import datetime

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
    logging.info(msg="Пользователь {0} очистил состояния!".format(message.from_user.full_name))
    await message.answer(text="Очистка была успешно проведена!")


@commands_router.message(Command("reg"))
async def com_reg(message: types.Message) -> None:
    """
    Асинхронный метод для обработки команды 'reg' -> производим регистрацию пользователя
    :param message:
    :return:
    """

    to_reg_data: tuple = message.from_user.full_name, message.from_user.id, datetime.datetime.now()
    logging.info(msg="Пользователь {0} вызвал команду reg".format(message.from_user.full_name))
    await message.answer(text="Вы были успешно зарегистрированы!")


@commands_router.message(Command("profile"))
async def com_profile(message: types.Message) -> None:
    """
    Асинхронный метод для доступа к личному профилю пользователя
    :param message:
    :return:
    """

    logging.info(msg="Пользователь {0} вызвал команду profile".format(message.from_user.full_name))
    await message.answer(text=f"Добро пожаловать в личный профиль {message.from_user.full_name}!")


@commands_router.message(Command("event"))
async def com_event(message: types.Message) -> None:
    """
    Асинхронный метод для обработки команды 'event', получаем от User название и по возможности коннектим
    :param message:
    :return:
    """

    logging.info(msg="Пользователь {0} вызвал команду event".format(message.from_user.full_name))
    await message.answer(text=f"Пожалуйста, введите название события")