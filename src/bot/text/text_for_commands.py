from emoji import emojize

async def get_message_start(user_full_name: str) -> str:
    text_start: str = emojize(":hand_with_fingers_splayed_dark_skin_tone: <b>Привет</b> {0}, я бот по району <i>'Богудония'</i>\n\n".format(user_full_name) +
                         "Я могу помочь тебе <b>создать событие</b>, <b>участвовать в событии</b>, <b>вносить экологический вклад</b>" +
                         " в район, а так же <b>зафиксировать непрестойные местоположения</b>" +
                         "\n\nДавай начнём :green_heart:, внесём свою лепту в экологическое процветание Богудонии!".format(user_full_name), language="en")

    return text_start


async def get_message_help() -> str:
    text_help: str = emojize("<b><i>Мой перечень команд :bullseye:: </i></b>\n\n" + \
        ":turtle: /start\tЗапуск Бота\n" + \
        ":turtle: /help\tПоддержка Бота\n", language="en")

    return text_help