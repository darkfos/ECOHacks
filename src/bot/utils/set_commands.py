#Aiogram
from aiogram import Bot
from aiogram.types import BotCommand

#Сторонние библиотеки
from emoji import emojize
async def set_commands(bot: Bot) -> None:

    ecobot_commands: list = [
        BotCommand(command="start", description=emojize(":turtle: Начало работы с ботом", language="en")),
        BotCommand(command="help", description=emojize(":turtle: Поддержка бота, команды", language="en")),
        BotCommand(command="report", description=emojize(string=":turtle: Отправка отчёта", language="en")),
        BotCommand(command="clear", description=emojize(string=":turtle: Очистка содержимого", language="en"))
    ]

    await bot.set_my_commands(commands=ecobot_commands)