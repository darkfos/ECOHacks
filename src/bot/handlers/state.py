# Aiogram
import datetime
import logging

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

#Локальные директивы
from src.bot.states import ReportUser
from src.data_cls import ReportInfo
from src import post_report, del_report, configuration

#Сторонние директивы
import requests

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

    if message.content_type == types.ContentType.PHOTO:

        # Кодировка данных
        photo_id = message.photo[-1].file_id

        # Обращаемся к сервису, получаем путь файла, относительно его ключа
        response_to_teg_api = requests.get(f"https://api.telegram.org/bot{configuration.API_KEY}/getFile?file_id={photo_id}")
        result = response_to_teg_api.json()["result"]["file_path"]

        # Обращаемся к сервису, получаем байт код
        img_byte = requests.get(f"https://api.telegram.org/file/bot{configuration.API_KEY}/{result}")
        itog_img = img_byte.content

        await state.update_data(photo_user=itog_img)
        await message.answer(text="Отлично. Жду гео данные!")
        await state.set_state(ReportUser.geo_position)
    else:
        await message.answer(text="Вы отправили не фото.")



@state_router.message(ReportUser.geo_position)
async def geo_position(message: types.Message, state: FSMContext) -> None:
    """
    Обработка состояния, гео данные от пользователя
    :param message:
    :param state:
    :return:
    """

    await state.update_data(geo_position=message.text)

    data_coroutine = list((await state.get_data()).values())
    data_to_add: ReportInfo = ReportInfo(message_history=data_coroutine[0], tg_id=data_coroutine[1], geo_position=data_coroutine[3], photo=data_coroutine[2], date_report=datetime.datetime.now())

    #Очистка состояния
    await state.clear()

    try:

        #Заносим данные в БД
        await post_report(data_report=data_to_add)


        await message.answer(text="Отлично, ваш отчёт был сохранён! Спасибо за ваш вклад")

    except Exception as ex:
        logging.exception(msg="Ошибка у пользователя {0} не смог отправить отчёт".format(message.from_user.id))
        await message.answer(text="К сожалению ваш отчёт не был сохранён. Внутреняя ошибка")