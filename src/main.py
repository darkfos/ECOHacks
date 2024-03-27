# Aiogram
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage


# Локальные директивы
from src import configuration
from src.bot import commands_router, state_router, message_router, set_commands, callback_router
from src import Database
from src.api.main import run_fast_app

# Сторонние библиотеки
import logging
import asyncio


async def start_application() -> None:
    """
    Запускаем приложения - (ТГ. Бота)
    :return:
    """

    #Подключаем логирование
    logging.basicConfig(level=logging.INFO)


    #Параметры запуска
    eco_bot: Bot = Bot(token=configuration.API_KEY)
    storage: MemoryStorage = MemoryStorage()
    dp_bot: Dispatcher = Dispatcher(bot=eco_bot, storage=storage)

    #Подключаемся и создаем таблицы БД
    Database()

    #Подключение роутеров
    dp_bot.include_routers(
        commands_router,
        state_router,
        message_router,
        callback_router,
    )

    #Устанавливаем список команд в меню подсказок
    await set_commands(bot=eco_bot)


    try:
        await dp_bot.start_polling(eco_bot)
        logging.info(msg="Бот начал свою работу")
    except Exception as ex:
        logging.critical(msg="Бот прекратил свою работу")


if __name__ == "__main__":
    try:
        run_fast_app()
        #asyncio.run(start_application())
    except KeyboardInterrupt as ki:
        logging.critical(msg="Бот остановил свою работу")
    except KeyError as ke:
        logging.critical(msg="Бот остановил свою работу")