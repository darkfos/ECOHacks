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
