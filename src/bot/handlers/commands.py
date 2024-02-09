# Aiogram

from aiogram import Router, types
from aiogram.filters import CommandStart

# Локальные директивы
...

# Сторонние библиотеки

commands_router: Router = Router()

@commands_router.message(CommandStart())
async def com_start(message: types.Message):
    await message.answer(text="Я родился")