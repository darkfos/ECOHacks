from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


async def get_geo_button() -> ReplyKeyboardMarkup:
    kb_btn: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отправить гео-данные", request_location=True)
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Отправить гео-данные",
        one_time_keyboard=True
    )

    return kb_btn