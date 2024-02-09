from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

async def get_profile_buttons():
    """
    Создаем кнопки для личного профиля
    :return:
    """

    keyboards: InlineKeyboardBuilder = InlineKeyboardBuilder()
    keyboards.add(InlineKeyboardButton(text="Создать событие"))
    keyboards.add(InlineKeyboardButton(text="Мои события"))
    keyboards.add(InlineKeyboardButton(text="Мой вклад"))

    return keyboards
